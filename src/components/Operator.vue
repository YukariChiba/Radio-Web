<template>
  <v-card>
    <v-card-title
      ><v-icon large left>mdi-account</v-icon>Operator Information</v-card-title
    >
    <v-list-item link>
      <v-list-item-avatar>
        <img :src="data.avatar" />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title class="text-h6">
          {{ data.name }}
        </v-list-item-title>
        <v-list-item-subtitle>i@0x7f.cc</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-divider />
    <v-card-actions>
      <v-btn
        color="primary"
        text
        v-for="l in data.links"
        :key="l.link"
        :href="l.link"
      >
        {{ l.title }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import data from "@/data.json";
export default {
  data: () => ({
    data: data.operator
  })
};
</script>
