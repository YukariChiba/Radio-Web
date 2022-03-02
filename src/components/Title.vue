<template>
  <v-card class="my-4">
    <v-card-title>
      <v-list-item two-line>
        <v-list-item-content>
          <v-list-item-title class="text-h2 text-center">
            <ScaleableText>
              <ruby v-for="(c, i) in data.callsign" :key="i">
                <b>{{ c }}</b
                ><rt class="text-h6">{{ charspell[c] }}</rt> &nbsp;
              </ruby>
            </ScaleableText>
          </v-list-item-title>
          <v-list-item-subtitle class="text-h5 text-center">
            {{ data.description }}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-card-title>
    <v-card-actions class="justify-center">
      <v-chip class="ma-2" color="primary" outlined label tag>
        <v-icon left>
          mdi-map-marker
        </v-icon>
        {{ data.locator }}
      </v-chip>
      <v-chip class="ma-2" color="success" outlined label tag>
        <v-icon left>
          mdi-license
        </v-icon>
        CN Class {{ data.class }}
      </v-chip>
      <v-chip class="ma-2" color="orange" outlined label tag>
        <v-icon left>
          mdi-school
        </v-icon>
        {{ data.location }}
      </v-chip>
    </v-card-actions>
  </v-card>
</template>

<script>
import data from "@/data.json";
import charspell from "@/data/charspell.json";

import ScaleableText from "@/components/ScaleableText";

export default {
  components: { ScaleableText },
  data: () => ({
    data: data,
    charspell: charspell
  })
};
</script>
