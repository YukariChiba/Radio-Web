<template>
  <v-data-table :headers="headers" :items="qsodata" :items-per-page="25">
    <template v-slot:item.region="{ item }">
      <country-flag
        :country="getinfo(item.callsign).areacode"
        size="normal"
        :rounded="true"
      />
    </template>
    <template v-slot:item.freq="{ item }">
      {{ item.freq }} ({{ item.band }})
    </template>
    <template v-slot:item.time="{ item }">
      {{ item.time }}
      <v-icon v-if="item.confirmed == 'Y'" right color="success"
        >mdi-check-circle</v-icon
      >
    </template>
  </v-data-table>
</template>

<script>
import moment from "moment";
import qsolog from "@/data/qso.json";
import callsign from "callsign";
import CountryFlag from "vue-country-flag";

export default {
  components: {
    CountryFlag
  },
  data: () => ({
    getinfo: callsign.getAmateurRadioInfoByCallsign,
    headers: [
      {
        text: "Region",
        align: "start",
        sortable: false,
        value: "region"
      },
      {
        text: "Callsign",
        align: "start",
        sortable: false,
        value: "callsign"
      },
      {
        text: "Frequency",
        align: "start",
        value: "freq"
      },
      {
        text: "Mode",
        align: "start",
        value: "mode"
      },
      {
        text: "Time",
        align: "start",
        value: "time"
      }
    ],
    qsolog: qsolog
  }),
  computed: {
    qsodata: function() {
      return this.qsolog.map(
        x =>
          new Object({
            callsign: x[0],
            band: x[1],
            freq: parseFloat(x[2]),
            mode: x[3],
            time: moment(x[4]).format("YYYY-MM-DD hh:mm"),
            confirmed: x[5]
          })
      );
    }
  }
};
</script>

<style></style>
