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
            <p>All logs will be uploaded to LOTW, HRDLOG and QRZ.</p>
            <h3>QSL Card Exchange</h3>
            <p>
                QSL card exchange is welcomed.<br />
                <b>QSL Card Postal Address</b>:<br />
                999 Gaoxin Blvd., Wuhan, P.R.China, 430223<br />
            </p>
            <v-alert
                color="warning"
                icon="$warning"
                variant="outlined"
                density="compact"
                title="Attention"
                text="The local post office has confirmed that it
   deliberately discards all ordinary mail, so to ensure the
   reliable delivery of your QSL card, it is important to send it
   by registered mail. Information and additional costs required
   for mailing can be requested by contacting us."
            ></v-alert>
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
            <p>所有通联日志都将被上传至 LOTW, HRDLOG 和 QRZ。</p>
            <h3>QSL 卡片交换</h3>
            <p>
                欢迎进行 QSL 卡片的交换。<br />
                <b>QSL 卡片邮寄地址</b>：<br />
                湖北省武汉市高新大道 999 号，430223<br />
            </p>
            <v-alert
                color="warning"
                icon="$warning"
                variant="outlined"
                density="compact"
                title="注意"
                text="本地邮政所已确认会故意丢弃所有平信，为确保您的 QSL
       卡的可靠送达，请务必使用挂号信寄送。邮寄所需要的信息和额外费用可以联系本台索要。"
            ></v-alert>
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
