<template>
    <v-card rounded="lg">
        <v-tabs
            slider-color="primary"
            v-model="tab"
            bg-color="transparent"
            grow
        >
            <v-tab value="about">
                <v-icon class="hidden-xs" start>mdi-pound</v-icon> About
            </v-tab>
            <v-tab value="log">
                <v-icon class="hidden-xs" start>mdi-notebook</v-icon> QSO Log
            </v-tab>
            <v-tab value="qslcardpreview">
                <v-icon class="hidden-xs" start>mdi-card-bulleted</v-icon> QSL
                Card
            </v-tab>
        </v-tabs>
        <v-window v-model="tab">
            <v-window-item value="about">
                <MainAbout />
            </v-window-item>
            <v-window-item value="log" style="overflow-x: auto">
                <CommLog />
            </v-window-item>
            <v-window-item value="qslcardpreview" style="overflow-x: auto">
                <QSLCardPreview />
            </v-window-item>
        </v-window>
    </v-card>
</template>

<script setup>
const tab = ref(null);
</script>
