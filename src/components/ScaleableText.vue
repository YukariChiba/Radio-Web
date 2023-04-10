<template>
  <svg
    width="100%"
    height="100%"
    :viewBox="viewbox"
    preserveAspectRatio="xMinYMin meet"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
  >
    <foreignObject width="100%" height="100%">
      <div xmlns="http://www.w3.org/1999/xhtml" style="text-align: center">
        <slot />
      </div>
    </foreignObject>
  </svg>
</template>

<script>
export default {
  props: ["h", "w"],
  computed: {
    viewbox() {
      let vw = 400;
      let vh = 100;
      if (this.h) vh = this.h;
      if (this.w) vw = this.w;
      return `0 0 ${vw} ${vh}`;
    },
  },
};
</script>

<style scoped>
svg {
  max-width: 500px;
}
</style>
