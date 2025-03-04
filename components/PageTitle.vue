<template>
    <v-card rounded="lg" class="my-4">
        <v-card-title>
            <v-list-item two-line>
                <v-list-item-title
                    class="text-h2 text-center mt-6"
                    style="line-height: 1"
                >
                    <ScaleableText :h="80">
                        <ruby
                            class="ml-2 mr-2"
                            v-for="(c, i) in data.callsign"
                            :key="i"
                        >
                            <b>{{ c }}</b
                            ><rt class="text-h6">{{ charspell[c] }}</rt>
                        </ruby>
                    </ScaleableText>
                </v-list-item-title>
                <v-list-item-subtitle class="pb-0 text-h5 text-center">
                    <ScaleableText :h="30">
                        {{ data.description }}
                    </ScaleableText>
                </v-list-item-subtitle>
            </v-list-item>
        </v-card-title>
        <v-card-actions style="flex-wrap: wrap" class="justify-center">
            <v-chip class="mr-2" color="primary" label>
                <v-icon start> mdi-map-marker </v-icon>
                {{ data.locator }}
            </v-chip>
            <v-chip class="mr-2" color="success" label>
                <v-icon start> mdi-license </v-icon>
                CN Class {{ data.class }}
            </v-chip>
            <v-chip class="mr-2" color="orange" label>
                <v-icon start> mdi-city </v-icon>
                {{ data.location }}
            </v-chip>
        </v-card-actions>
    </v-card>
</template>

<script setup>
import data from "@/assets/data.json";
import charspell from "@/assets/charspell.json";
</script>
