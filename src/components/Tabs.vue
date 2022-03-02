<template>
  <v-card>
    <v-tabs
      slider-color="primary"
      v-model="tab"
      background-color="transparent"
      color="basil"
      grow
    >
      <v-tab> <v-icon left>mdi-pound</v-icon> About </v-tab>
      <v-tab> <v-icon left>mdi-notebook</v-icon> QSO Log </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <About />
      </v-tab-item>
      <v-tab-item>
        <Log />
      </v-tab-item>
    </v-tabs-items>
  </v-card>
</template>

<script>
import About from "@/components/About";
import Log from "@/components/Log";
export default {
  data: () => ({
    tab: null
  }),
  components: {
    About,
    Log
  }
};
</script>

<style></style>
