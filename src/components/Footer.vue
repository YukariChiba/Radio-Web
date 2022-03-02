<template>
  <v-card>
    <v-card-text class="text-center">
      &copy; {{ data.callsign }} {{ date }}
    </v-card-text>
  </v-card>
</template>

<script>
import data from "@/data.json";

export default {
  data: () => ({
    data: data,
    date: new Date().getFullYear()
  })
};
</script>
