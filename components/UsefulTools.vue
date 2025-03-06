<template>
    <v-card rounded="lg">
        <v-card-title
            ><v-icon large start>mdi-tools</v-icon>Useful Tools</v-card-title
        >
        <v-card-actions>
            <v-btn
                color="primary"
                v-for="l in data"
                :key="l.link"
                :href="l.link"
                v-text="l.title"
            />
        </v-card-actions>
    </v-card>
</template>

<script setup>
import d from "@/assets/data.json";
const data = d.tools;
</script>

<style scoped>
.v-list {
    background: unset !important;
}
</style>
