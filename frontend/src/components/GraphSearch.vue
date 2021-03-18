<template>
    <div>
        <v-row
                justify="center"
                class="green text-center"
                style="padding-top: 100px;"
        >
            <v-col cols="6" align-self="center">
                <div class="text-h2 white--text py-8">QQ图像化查询</div>
                <div class="white--text py-sm-10">输入QQ号，图像化展示加入的群和群内成员</div>
            </v-col>
        </v-row>
        <v-row
                justify="center"
                class="white text-center">
            <v-col cols="6">
                <div>
                    <v-text-field
                            outlined
                            type="text"
                            label=""
                            prepend-inner-icon="mdi-magnify"
                            color="green"
                            v-model="searchText"
                            @click:prepend-inner="sendMessage"
                            @keydown.enter="sendMessage"
                    />
                </div>
            </v-col>
        </v-row>

        <v-row
                justify="center"
                class="text-center"
        >
            <v-col cols="6" align-self="center">
                <div id="relationGraph" style="width: 100%;height:520px;"></div>
                <div class="content"></div>
            </v-col>
        </v-row>

        <template>
            <div class="text-center ma-2">
                <v-snackbar
                        v-model="snackbar"
                        timeout="1000"
                        color="green"
                >
                    没有此用户信息
                    <template v-slot:action="{ attrs }">
                        <v-btn
                                color="white"
                                text
                                v-bind="attrs"
                                @click="snackbar = false"
                        >
                            ×
                        </v-btn>
                    </template>
                </v-snackbar>
            </div>
        </template>

    </div>
</template>

<script>
    export default {
        name: "GraphSearch",
        data() {
            return {
                test: "",
                searchText: "",
                snackbar: false,
            }
        },
        methods: {
            sendMessage() {
                var thiz = this
                if (thiz.searchText === '') {
                    return
                }

                this.axios.get("http://127.0.0.1:2333/query/relation?qqnum=" + thiz.searchText).then(response => {
                        let result_data = response.data
                        if (result_data.code !== '1') {
                            return
                        }
                        if (result_data.graph.links.length === 0) {
                            console.log("没有此用户信息")
                            thiz.snackbar = true
                            return;
                        }
                        thiz.drawChart(result_data.graph);
                    }
                ).catch(response => {
                    console.log(response)
                })
            },
            drawChart(webkitDep = require('../assets/test2')) {
                // 基于准备好的dom，初始化echarts实例
                let myChart = this.$echarts.init(document.getElementById("relationGraph"));
                myChart.showLoading()
                // 指定图表的配置项和数据
                // let webkitDep = require('../assets/test2')
                let option = {
                    legend: {
                        data: ['群主', '管理员', '一般成员', '查询用户']
                    },
                    series: [{
                        type: 'graph',
                        layout: 'force',
                        animation: false,
                        label: {
                            position: 'right',
                            formatter: '{b}'
                        },
                        draggable: true,
                        data: webkitDep.nodes.map(function (node, idx) {
                            node.id = idx;
                            return node;
                        }),
                        categories: webkitDep.categories,
                        force: {
                            edgeLength: 5,
                            repulsion: 20,
                            gravity: 0.2
                        },
                        edges: webkitDep.links
                    }]
                };
                // 使用刚指定的配置项和数据显示图表。
                myChart.hideLoading()
                myChart.setOption(option);
                window.addEventListener("resize", function () {
                    myChart.resize();  //页面大小变化后Echarts也更改大小
                });
            }

        },
        mounted() {
            document.querySelector("#relationGraph").style.width = document.querySelector(".content").clientWidth;
        }
    }
</script>

<style scoped>

</style>