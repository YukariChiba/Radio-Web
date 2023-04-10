<template>
  <v-card rounded="lg">
    <v-card-title
      ><v-icon large start>mdi-account</v-icon>Operator
      Information</v-card-title
    >
    <v-list density="comfortable" lines="two">
      <v-list-item
        link
        :prepend-avatar="data.avatar"
        :title="data.name"
        subtitle="i@0x7f.cc"
      >
      </v-list-item>
    </v-list>
    <v-divider />
    <v-card-actions>
      <v-btn
        color="primary"
        v-for="l in data.links"
        :key="l.link"
        :href="l.link"
        v-text="l.title"
      />
    </v-card-actions>
  </v-card>
</template>

<script>
import data from "@/data.json";
export default {
  data: () => ({
    data: data.operator,
  }),
};
</script>

<style scoped>
.v-list {
  background: unset !important;
}
</style>
