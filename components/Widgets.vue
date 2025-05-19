<template>
    <v-card rounded="lg">
        <v-card-title
            ><v-icon large start>mdi-widgets</v-icon>Widgets</v-card-title
        >
        <v-img
            src="https://hamalert.org/myspot?c=BH8AEA&h=dc7ee3562aa2a07e&hr=1"
            max-width="300px"
            class="img-light"
        />
        <v-img
            src="https://www.hamqsl.com/solar2.php?bgcolor=white&back=transparent"
            max-width="300px"
            class="img-light"
        />
        <v-img
            src="https://hamalert.org/myspot?c=BH8AEA&h=dc7ee3562aa2a07e&hr=1&dark=1"
            max-width="300px"
            class="img-dark"
        />
        <v-img
            src="https://www.hamqsl.com/solar2.php?bgcolor=black&back=transparent"
            max-width="300px"
            class="img-dark"
        />
    </v-card>
</template>

<style scoped>
.v-theme--light .img-dark {
    display: none;
}

.v-theme--dark .img-light {
    display: none;
}
</style>
