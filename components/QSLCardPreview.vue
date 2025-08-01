<template>
    <v-row no-gutters>
        <v-col cols="12" lg="6" xxl="4">
            <v-carousel>
                <template v-for="qslcard in data" :key="qslcard.title">
                    <template
                        v-for="cardtype in ['front', 'back']"
                        :key="cardtype"
                    >
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
        </v-col>
        <v-col cols="12" lg="6">
            <v-card-text>
                <h2>English Version</h2>
                <p>
                    This is my first version of QSL card. The front of the card
                    is a sheep, which is the same image as my homepage (<a
                        href="https://ewe.moe"
                        >ewe.moe</a
                    >), since I am often referred to as ‘sheep’.
                </p>
                <p>
                    The card is open source on GitHub at
                    <a href="https://github.com/YukariChiba/qsl"
                        >YukariChiba/qsl</a
                    >。
                </p>
            </v-card-text>
            <v-divider />
            <v-card-text>
                <h2>中文版</h2>
                <p>
                    这是我的第一个版本的 QSL
                    卡片。卡片的正面是一只羊，与我的主页 (<a
                        href="https://ewe.moe"
                        >ewe.moe</a
                    >) 的画面相同，因为经常有人以“羊”称呼我。
                </p>
                <p>
                    该卡片已在 GitHub 上开源，地址为
                    <a href="https://github.com/YukariChiba/qsl"
                        >YukariChiba/qsl</a
                    >。
                </p>
            </v-card-text>
        </v-col>
    </v-row>

    <v-divider />

    <div class="mt-2">
        <v-card-text>
            <h2>Active Card Sending Policy / 主动发卡策略</h2>
            <v-table>
                <thead>
                    <tr>
                        <th></th>
                        <th>Unique DXCC QSO</th>
                        <th>Unique QSO</th>
                        <th>Usual QSO</th>
                        <th>Usual QSO (Non-initial Exchange)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Digital</td>
                        <td>
                            <v-icon icon="mdi-check-decagram" color="success" />
                            100%
                        </td>
                        <td>
                            <v-icon icon="mdi-check-circle" color="success" />
                            Most
                        </td>
                        <td>
                            <v-icon icon="mdi-help-circle" color="warning" />
                            Uncertain
                        </td>
                        <td>
                            <v-icon icon="mdi-minus-circle" color="error" />
                            Passive
                        </td>
                    </tr>
                    <tr>
                        <td>Voice</td>
                        <td>
                            <v-icon icon="mdi-check-decagram" color="success" />
                            100%
                        </td>
                        <td>
                            <v-icon icon="mdi-check-decagram" color="success" />
                            100%
                        </td>
                        <td>
                            <v-icon icon="mdi-check-circle" color="success" />
                            Most
                        </td>
                        <td>
                            <v-icon icon="mdi-help-circle" color="warning" />
                            Uncertain
                        </td>
                    </tr>
                    <tr>
                        <td>CW</td>
                        <td>
                            <v-icon icon="mdi-check-decagram" color="success" />
                            100%
                        </td>
                        <td>
                            <v-icon icon="mdi-check-decagram" color="success" />
                            100%
                        </td>
                        <td>
                            <v-icon icon="mdi-check-circle" color="success" />
                            Most
                        </td>
                        <td>
                            <v-icon icon="mdi-help-circle" color="warning" />
                            Uncertain
                        </td>
                    </tr>
                </tbody>
            </v-table>
        </v-card-text>
    </div>

    <v-divider />

    <div class="mt-2">
        <v-card-text>
            <h2>Card Log</h2>
            <h3>
                Received
                <v-chip class="ml-2" size="x-small" label>{{
                    q.cfm.length
                }}</v-chip>
            </h3>
            <p>
                <v-chip
                    label
                    variant="text"
                    v-for="cs in q.cfm.sort()"
                    :key="cs"
                >
                    <v-icon
                        left
                        icon="mdi-swap-horizontal"
                        v-if="q.sent.includes(cs)"
                    />{{ cs }}
                </v-chip>
            </p>
            <h3>
                Sent
                <v-chip class="ml-2" size="x-small" label>{{
                    q.sent.length
                }}</v-chip>
            </h3>
            <p>
                <v-chip
                    label
                    variant="text"
                    v-for="cs in q.sent.sort()"
                    :key="cs"
                >
                    <v-icon
                        left
                        icon="mdi-swap-horizontal"
                        v-if="q.cfm.includes(cs)"
                    />{{ cs }}
                </v-chip>
            </p>
            <h3>
                Received (Eyeball)
                <v-chip class="ml-2" size="x-small" label>{{
                    q.eye.length
                }}</v-chip>
            </h3>
            <p>
                <v-chip
                    label
                    variant="text"
                    v-for="cs in q.eye.sort()"
                    :key="cs"
                >
                    {{ cs }}
                </v-chip>
            </p>
        </v-card-text>
    </div>
</template>

<script setup>
import d from "@/assets/data.json";
import q from "@/assets/qsl.json";
const data = d.qslcards;
</script>

<style>
.v-carousel .v-btn {
    background: rgba(var(--v-theme-surface), 0.4);
    backdrop-filter: blur(4px);
}
</style>

<style scoped>
p,
h1,
h2,
h3,
h4,
h5,
h6 {
    line-height: 2rem;
}
</style>
