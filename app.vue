<template>
    <NuxtLayout>
        <v-app>
            <BackGround />
            <FabButton />
            <v-container>
                <NuxtPage />
            </v-container>
        </v-app>
    </NuxtLayout>
</template>

<script setup>
useHead({
    title: "BH8AEA | Amateur Radio Station",
    meta: [
        { name: "description", content: "Just another amateur radio station." },
        { name: "og:title", content: "BH8AEA | Amateur Radio Station" },
        { name: "og:site_name", content: "BH8AEA | Amateur Radio Station" },
        { name: "og:url", content: "https://radio.0x7f.cc" },
        {
            name: "og:description",
            content: "Just another amateur radio station.",
        },
        { name: "og:type", content: "website" },
        { name: "og:image", content: "/og.png" },
    ],
});
</script>
