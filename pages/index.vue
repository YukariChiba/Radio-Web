<template>
    <div class="d-flex flex-column">
        <PageTitle class="ma-2" />
        <div class="d-flex mt-2 flex-wrap flex-sm-nowrap">
            <div
                class="d-flex flex-column order-3 order-sm-1 flex-grow-1 flex-sm-grow-0 sidebar"
            >
                <OperatorInfo class="ma-2" />
                <DeviceList class="ma-2" />
                <Widgets class="ma-2" />
                <UsefulTools class="ma-2" />
                <PageFooter class="ma-2" />
            </div>
            <div class="d-flex flex-column order-1 order-sm-3 flex-grow-1">
                <MainTabs class="ma-2" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.sidebar {
    max-width: 560px;
}

.v-card {
    background: rgba(var(--v-theme-surface), 0.8);
    backdrop-filter: blur(4px);
}
</style>
