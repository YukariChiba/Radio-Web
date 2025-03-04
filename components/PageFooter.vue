<template>
    <v-card rounded="lg">
        <v-card-text class="text-center">
            &copy; {{ data.callsign }} {{ new Date().getFullYear() }}
        </v-card-text>
    </v-card>
</template>

<script setup>
import data from "@/assets/data.json";
</script>
