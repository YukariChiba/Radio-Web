<template>
  <v-card rounded="lg">
    <v-card-title>
      <v-icon large start>mdi-radio-tower</v-icon>
      RIG Information
    </v-card-title>
    <v-list lines="three">
      <v-list-item
        link
        v-for="(d, i) in data"
        :key="i"
        :disabled="!d.status"
        :title="d.name + (d.status ? '' : '(Unavailable)')"
        :subtitle="d.power + ' Watt | Antenna: ' + d.ant"
      >
        <template v-slot:prepend>
          <v-avatar color="grey">
            <v-icon color="white">mdi-antenna</v-icon>
          </v-avatar>
        </template>
        <v-chip
          size="x-small"
          label
          color="primary"
          v-for="t in d.type"
          :key="t"
          class="mx-1"
        >
          {{ t }}
        </v-chip>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
import data from "@/data.json";
export default {
  data: () => ({
    data: data.devices,
  }),
};
</script>

<style scoped>
.v-list {
  background: unset !important;
}
</style>
