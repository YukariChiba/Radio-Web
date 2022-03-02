<template>
  <svg
    width="100%"
    height="100%"
    viewBox="0 0 400 100"
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

<style scoped>
svg {
  max-width: 500px;
}
</style>
