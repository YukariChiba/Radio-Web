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
        :country="getinfo(item.raw.callsign).areacode"
        v-if="getinfo(item.raw.callsign)"
        size="normal"
        :rounded="true"
      />
      <v-icon v-else icon="mdi-help-box"></v-icon>
    </template>
    <template v-slot:item.callsign_m="{ item }">
      <country-flag
        class="elevation-4 mr-1"
        :country="getinfo(item.raw.callsign).areacode"
        v-if="getinfo(item.raw.callsign)"
        size="small"
        :rounded="true"
      />
      <v-icon v-else icon="mdi-help-box" start></v-icon>
      <v-icon
        start
        v-if="item.raw.confirmed == 'Y'"
        color="success"
        size="small"
        >mdi-check-circle</v-icon
      >
      <small>{{ item.raw.callsign }}</small>
    </template>
    <template v-slot:item.freq="{ item }">
      {{ item.raw.freq }} ({{ item.raw.band }})
    </template>
    <template v-slot:item.freq_m="{ item }">
      {{ item.raw.band }}
    </template>
    <template v-slot:item.checked="{ item }">
      <v-icon v-if="item.raw.confirmed == 'Y'" color="success"
        >mdi-check-circle</v-icon
      >
    </template>
  </v-data-table>
</template>

<script>
import { VDataTable } from "vuetify/labs/VDataTable";
import moment from "moment";
import qsolog from "@/data/qso.json";
import callsign from "callsign";
import CountryFlag from "vue-country-flag-next";
import { useDisplay } from "vuetify";

export default {
  components: {
    CountryFlag,
    VDataTable,
  },
  setup() {
    const { mdAndUp } = useDisplay();
    return { mdAndUp };
  },
  data: () => ({
    getinfo: callsign.getAmateurRadioInfoByCallsign,
    headers_mobile: [
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
    ],
    headers: [
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
    ],
    qsolog: qsolog,
  }),
  computed: {
    qsodata: function () {
      return this.qsolog.map(
        (x) =>
          new Object({
            callsign: x[0],
            band: x[1],
            freq: parseFloat(x[2]),
            mode: x[3],
            time: moment(x[4]).format("YYYY-MM-DD hh:mm"),
            confirmed: x[5],
          })
      );
    },
  },
};
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
