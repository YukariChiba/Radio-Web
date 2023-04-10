<template>
  <v-data-table :headers="headers" :items="qsodata" :items-per-page="25">
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
    <template v-slot:item.freq="{ item }">
      {{ item.raw.freq }} ({{ item.raw.band }})
    </template>
    <template v-slot:item.time="{ item }">
      {{ item.time }}
      <v-icon v-if="item.raw.confirmed == 'Y'" end color="success"
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

export default {
  components: {
    CountryFlag,
    VDataTable,
  },
  data: () => ({
    getinfo: callsign.getAmateurRadioInfoByCallsign,
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
