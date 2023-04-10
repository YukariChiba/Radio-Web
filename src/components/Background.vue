<template>
  <div class="bg" :style="{ 'background-image': 'url(' + bg + ')' }" />
</template>

<script>
import bg from "@/assets/bg.svg";
import { useTheme } from "vuetify";
export default {
  data: () => ({
    bg: bg,
  }),
  setup() {
    const theme = useTheme();
    return {
      getTheme: () => {
        return theme.global.name.value;
      },
    };
  },
};
</script>

<style>
.bg {
  opacity: 0.5;
  background: fixed;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  background-attachment: fixed;
}
</style>
