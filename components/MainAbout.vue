<template>
    <div>
        <div class="float-right">
            <v-img
                class="mr-3 hidden-sm-and-down"
                src="https://www.hamqsl.com/solar2.php?bgcolor=white&back=transparent"
            />
        </div>
        <v-card-title class="mb-4">
            <v-icon large start>mdi-pound</v-icon>
            About
        </v-card-title>
        <v-card-text>
            <h2>English Version</h2>
            <p>
                Hello, this BH8AEA. Welcome to the page of this radio station.
            </p>
            <p>
                Class A license since 2021.05. Class B license since 2022.1.
                Founder and member of UESTC Amateur Radio Association.
            </p>
            <h3>QSO Log Info</h3>
            <p>
                All logs will be uploaded to LOTW, HRDLOG and QRZ in 72 hrs. If
                your record has not been uploaded, please contact me.
            </p>
            <h3>QSL Card Exchange</h3>
            <p>QSL card exchange is welcomed.</p>
            <p>
                All cards received will be replied to, SASE is not required, it
                is recommended to provide your address in the mail.
            </p>
            <v-alert
                density="compact"
                title="QSL Card Postal Address (Public, Receive):"
            >
                YUKARI<br />
                P.O. Box 399-5, HuiNan Post Office<br />
                Shanghai, P.R.China 201399<br />
                +86-21-58223996
            </v-alert>
        </v-card-text>
        <v-divider />
        <v-card-text>
            <h2>中文版</h2>
            <p>您好，这里是 BH8AEA。欢迎来到本电台的页面。</p>
            <p>
                2021.5 获得 A 证，2022.1 获得 B 证，是 UESTC
                业余无线电协会建立者兼成员。
            </p>
            <h3>通联日志</h3>
            <p>
                所有通联日志都将在 72 小时内被上传至 LOTW, HRDLOG 和
                QRZ，如果您的记录未被上传，请与我联系。
            </p>
            <h3>QSL 卡片交换</h3>
            <p>欢迎进行 QSL 卡片的交换。</p>
            <p>
                收到的所有卡片都会回复，SASE
                不是必需，但是建议信件内附您的地址。
            </p>
            <v-alert density="compact" title="QSL 卡片邮寄地址（公开，接收）:">
                YUKARI（收）<br />
                上海市 399-5 邮政信箱<br />
                邮编：201399<br />
                021-58223996
            </v-alert>
        </v-card-text>
    </div>
</template>

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
