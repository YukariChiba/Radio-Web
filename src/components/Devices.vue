<template>
  <v-card>
    <v-card-title>
      <v-icon large left>mdi-radio-tower</v-icon>
      RIG Information
    </v-card-title>
    <v-list>
      <v-list-item link v-for="(d, i) in data" :key="i" :disabled="!d.status">
        <v-list-item-icon>
          <v-icon large>mdi-antenna</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            {{ d.name }} {{ d.status ? "" : "(Unavailable)" }}
          </v-list-item-title>
          <v-list-item-action-text>
            {{ d.power }} Watt | Antenna: {{ d.ant }}
          </v-list-item-action-text>
          <v-list-item-action-text>
            <v-chip
              color="primary"
              outlined
              v-for="t in d.type"
              :key="t"
              small
              class="mx-1"
            >
              {{ t }}
            </v-chip>
          </v-list-item-action-text>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script>
import data from "@/data.json";
export default {
  data: () => ({
    data: data.devices
  })
};
</script>

<style></style>
