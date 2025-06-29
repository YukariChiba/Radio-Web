<template>
    <v-alert
        v-if="!loading && qsodata.length == 0"
        class="ma-2"
        variant="outlined"
        color="warning"
        icon="mdi-alert-outline"
        title="Things happen that shouldn't happen"
        text="No QSO data was obtained, but this is not possible, and a reasonable explanation is that the LOTW is down or under maintenance, or that there is a problem with your network."
    />
    <v-data-table
        :loading="loading"
        width="100%"
        :headers="mdAndUp ? headers : headers_mobile"
        :items="qsodata"
        :items-per-page="25"
    >
        <template v-slot:item.region="{ item }">
            <country-flag
                class="elevation-4"
                :country="getinfo(item.callsign).areacode"
                v-if="getinfo(item.callsign)"
                size="normal"
                :rounded="true"
            />
            <v-icon v-else icon="mdi-help-box"></v-icon>
        </template>
        <template v-slot:item.callsign_m="{ item }">
            <country-flag
                class="elevation-4 mr-1"
                :country="getinfo(item.callsign).areacode"
                v-if="getinfo(item.callsign)"
                size="small"
                :rounded="true"
            />
            <v-icon v-else icon="mdi-help-box" start></v-icon>
            <v-icon
                start
                v-if="item.confirmed == 'Y'"
                color="success"
                size="small"
                >mdi-check-circle</v-icon
            >
            <small>{{ item.callsign }}</small>
        </template>
        <template v-slot:item.callsign="{ item }">
            <v-chip
                label
                class="font-weight-bold"
                :ripple="false"
                :href="`https://www.qrz.com/db/${item.callsign}`"
                :text="item.callsign"
            />
        </template>
        <template v-slot:item.freq="{ item }">
            {{ item.freq }} ({{ item.band }})
        </template>
        <template v-slot:item.freq_m="{ item }">
            {{ item.band }}
        </template>
        <template v-slot:item.checked="{ item }">
            <v-icon v-if="item.confirmed == 'Y'" color="success"
                >mdi-check-circle</v-icon
            >
        </template>
    </v-data-table>
</template>

<script setup>
import moment from "moment";
import callsign from "callsign";
import CountryFlag from "vue-country-flag-next";
import { useDisplay } from "vuetify";

const { mdAndUp } = useDisplay();
const getinfo = callsign.getAmateurRadioInfoByCallsign;
const qsolog = ref([]);
const loading = ref(true);
const headers_mobile = [
    {
        title: "Callsign",
        align: "start",
        sortable: false,
        key: "callsign_m",
    },
    {
        title: "Frequency",
        align: "start",
        key: "freq_m",
    },
    {
        title: "Mode",
        align: "start",
        key: "mode",
    },
];
const headers = [
    {
        title: "Region",
        align: "start",
        sortable: false,
        key: "region",
    },
    {
        title: "Callsign",
        align: "start",
        sortable: false,
        key: "callsign",
    },
    {
        title: "Frequency",
        align: "start",
        key: "freq",
    },
    {
        title: "Mode",
        align: "start",
        key: "mode",
    },
    {
        title: "Time",
        align: "start",
        key: "time",
    },
    {
        title: "",
        align: "center",
        key: "checked",
    },
];

const qsodata = computed(() => {
    return qsolog.value.map(
        (x) =>
            new Object({
                callsign: x[0],
                band: x[1],
                freq: parseFloat(x[2]),
                mode: x[3],
                time: moment(x[4]).format("YYYY-MM-DD hh:mm"),
                confirmed: x[5],
            }),
    );
});

const fetchData = async () => {
    const response = await fetch(
        "https://yukarichiba.github.io/Radio-Web/qso.json",
    );
    qsolog.value = await response.json();
    loading.value = false;
};

fetchData();
</script>

<style scoped>
.v-table {
    background: unset !important;
}
</style>

<style>
tr,
th,
td {
    background: unset !important;
}
</style>
