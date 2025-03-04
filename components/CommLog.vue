<template>
    <v-data-table
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
import qsolog from "@/assets/qso.json";
import callsign from "callsign";
import CountryFlag from "vue-country-flag-next";
import { useDisplay } from "vuetify";

const { mdAndUp } = useDisplay();
const getinfo = callsign.getAmateurRadioInfoByCallsign;
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
    return qsolog.map(
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
