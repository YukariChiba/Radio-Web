<template>
    <v-carousel>
        <template v-for="qslcard in data" :key="qslcard.title">
            <template v-for="cardtype in ['front', 'back']" :key="cardtype">
                <v-carousel-item
                    v-if="cardtype in qslcard"
                    :src="qslcard[cardtype]"
                    class="justify-center"
                >
                    <div
                        style="
                            height: 100%;
                            align-content: center;
                            mix-blend-mode: multiply;
                        "
                        class="font-weight-bold text-center text-h1 text-grey"
                    >
                        Sample
                    </div>
                </v-carousel-item>
            </template>
        </template>
    </v-carousel>
</template>

<script setup>
import d from "@/assets/data.json";
const data = d.qslcards;
</script>

<style>
.v-carousel .v-btn {
    background: rgba(var(--v-theme-surface), 0.4);
    backdrop-filter: blur(4px);
}
</style>
