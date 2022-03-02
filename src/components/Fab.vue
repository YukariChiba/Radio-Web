<template>
  <v-btn
    fab
    fixed
    right
    bottom
    class="ma-6"
    @click="$vuetify.theme.dark = !$vuetify.theme.dark"
  >
    <v-icon>mdi-brightness-6</v-icon>
  </v-btn>
</template>

<script>
export default {};
</script>

<style></style>
