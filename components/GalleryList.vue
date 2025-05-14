<template>
    <v-slide-group class="pa-4 hidden-md-and-down" show-arrows>
        <v-slide-group-item v-for="i in g" :key="i.img">
            <v-card
                variant="tonal"
                class="ma-2"
                max-width="900px"
                max-height="300px"
            >
                <v-row no-gutters>
                    <v-col cols="12" lg="6">
                        <v-img :src="'/gallery/' + i.img" />
                    </v-col>
                    <v-col
                        cols="12"
                        lg="6"
                        style="overflow-y: scroll; max-height: 300px"
                    >
                        <v-card-title>Gallery: {{ i.title }}</v-card-title>
                        <v-card-text>
                            <p v-for="t in i.text" :key="t">{{ t }}</p>
                        </v-card-text>
                    </v-col>
                </v-row>
            </v-card>
        </v-slide-group-item>
    </v-slide-group>
</template>

<script setup>
import g from "@/assets/gallery.json";
</script>

<style scoped>
p,
h1,
h2,
h3,
h4,
h5,
h6 {
    line-height: 1.5rem;
}
</style>
