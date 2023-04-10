<template>
  <v-card rounded="lg">
    <v-tabs slider-color="primary" v-model="tab" bg-color="transparent" grow>
      <v-tab value="about"> <v-icon start>mdi-pound</v-icon> About </v-tab>
      <v-tab value="log"> <v-icon start>mdi-notebook</v-icon> QSO Log </v-tab>
    </v-tabs>
    <v-window v-model="tab">
      <v-window-item value="about">
        <About />
      </v-window-item>
      <v-window-item value="log">
        <Log />
      </v-window-item>
    </v-window>
  </v-card>
</template>

<script>
import About from "@/components/About";
import Log from "@/components/Log";
export default {
  data: () => ({
    tab: null,
  }),
  components: {
    About,
    Log,
  },
};
</script>

<style></style>
