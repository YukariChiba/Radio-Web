<template>
    <v-fab
        app
        rounded="lg"
        @click="toggleTheme"
        icon="mdi-brightness-6"
        size="large"
        color="primary"
        elevation="8"
        location="right bottom"
    />
</template>

<script setup>
import { useTheme } from "vuetify";
const theme = useTheme();
const toggleTheme = () =>
    (theme.global.name.value = theme.global.current.value.dark
        ? "light"
        : "dark");
</script>
