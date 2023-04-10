<template>
  <VLayoutItem model-value position="bottom" class="text-end" size="108">
    <div>
      <VBtn
        class="ma-6"
        rounded="lg"
        @click="toggleTheme"
        icon="mdi-brightness-6"
        size="large"
        color="primary"
        elevation="8"
      />
    </div>
  </VLayoutItem>
</template>

<script setup>
import { useTheme } from "vuetify";
const theme = useTheme();
const toggleTheme = () =>
  (theme.global.name.value = theme.global.current.value.dark
    ? "light"
    : "dark");
</script>
