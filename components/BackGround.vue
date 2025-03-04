<template>
    <div class="bg">
        <v-img class="bg-img" :src="bg" cover />
    </div>
</template>

<script setup>
import bg from "@/assets/bg.svg";
import { useTheme } from "vuetify";
const theme = useTheme();
const getTheme = () => {
    return theme.global.name.value;
};
</script>

<style>
.bg-img {
    height: 100%;
    width: 100%;
}

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
