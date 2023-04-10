<template>
  <v-app>
    <Background />
    <Fab />
    <v-main>
      <v-container>
        <div class="d-flex flex-column">
          <MainTitle class="ma-2" />
          <div class="d-flex mt-2 flex-wrap flex-sm-nowrap">
            <div
              class="d-flex flex-column order-3 order-sm-1 flex-grow-1 sidebar"
            >
              <OperatorInfo class="ma-2" />
              <DevicesInfo class="ma-2" />
              <MainFooter class="ma-2" />
            </div>
            <div class="d-flex flex-column order-1 order-sm-3 flex-grow-1">
              <Tabs class="ma-2" />
            </div>
          </div>
        </div>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import data from "@/data.json";
import charspell from "@/data/charspell.json";

import Background from "@/components/Background";
import MainTitle from "@/components/Title";
import OperatorInfo from "@/components/Operator";
import DevicesInfo from "@/components/Devices";
import MainFooter from "@/components/Footer";
import Tabs from "@/components/Tabs";
import Fab from "@/components/Fab";

export default {
  name: "App",
  components: {
    Background,
    MainTitle,
    OperatorInfo,
    DevicesInfo,
    Tabs,
    Fab,
    MainFooter,
  },
  data: () => ({
    data: data,
    charspell: charspell,
  }),
};
</script>

<style scoped>
.sidebar {
  max-width: 560px;
}

.v-card {
  background: rgba(var(--v-theme-surface), 0.8);
  backdrop-filter: blur(4px);
}
</style>
