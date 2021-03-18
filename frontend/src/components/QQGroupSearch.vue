<template>
    <div>
        <div>
            <v-row
                    justify="center"
                    class="green text-center"
                    style="padding-top: 100px;"
            >
                <v-col cols="6" align-self="center">
                    <div class="text-h2 white--text py-8">QQ群社工库查询</div>
                    <div class="white--text py-sm-10">查询qq号加入的QQ群，和QQ群内成员信息</div>
                </v-col>
            </v-row>
            <v-row
                    justify="center"
                    class="white text-center">
                <v-col cols="1">
                    <v-select
                            :items="selectItem"
                            outlined
                            label="类别"
                            color="green"
                            v-model="searchLabel"
                    >
                    </v-select>
                </v-col>
                <v-col cols="4">
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
        </div>

        <div>
            <v-data-table
                    :headers="headers"
                    :items="desserts"
                    :page.sync="page"
                    :items-per-page="itemsPerPage"
                    :loading="loading"
                    hide-default-footer
                    class="elevation-1"
                    @page-count="pageCount = $event"
            />
            <div class="text-center pt-2">
                <v-pagination
                        v-model="page"
                        :length="pageCount"
                        color="green"
                />
            </div>
        </div>

        <template>
            <div class="text-center ma-2">
                <v-snackbar
                        v-model="snackbar"
                        timeout="1000"
                        color="green"
                >
                    没有相关信息
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
        name: "QQGroupSearch",
        data() {
            return {
                selectItem: ['QQ号', 'Q群号'],
                test: "",
                searchLabel: "",
                searchText: "",
                page: 1,
                pageCount: 0,
                itemsPerPage: 5,
                loading: false,
                snackbar: false,
                headers: [
                    {text: 'QQ群号', align: 'start', value: 'QunNum',},
                    {text: 'QQ号', value: 'QQNum'},
                    {text: '昵称', sortable: false, value: 'Nick'},
                    {text: '性别', sortable: false, value: 'Gender'},
                ],
                desserts: [],
            }
        },
        methods: {
            click() {
                this.searchText = "213"
            },
            sendMessage() {
                let thiz = this
                if (thiz.searchLabel === '' || thiz.searchText === '') {
                    return
                }
                this.loading = true
                let label = ""
                if (thiz.searchLabel === thiz.selectItem[0]) {
                    label = 'qq'
                } else if (thiz.searchLabel === thiz.selectItem[1]) {
                    label = 'qqgroup'
                } else {
                    thiz.dialog = true
                }
                this.axios.get("http://127.0.0.1:2333/query/" + label + "?num=" + thiz.searchText).then((response) => {
                    let result_data = response.data
                    if (result_data.code !== '1') {
                        return
                    }
                    let array = [];
                    let result = result_data.res
                    for (let i = 0; i < result.length; i++) {
                        let element = {};
                        element.QunNum = result[i].QunNum;
                        element.QQNum = result[i].QQNum;
                        element.Nick = result[i].Nick;
                        element.Gender = result[i].Gender === '0' ? '男' : '女';
                        array.push(element)
                    }
                    if (array.length === 0) {
                        thiz.snackbar = true
                    }
                    console.log(array)
                    thiz.desserts = array;
                    thiz.loading = false;
                }).catch(() => {
                    thiz.loading = false
                })
            }
        }
    }
</script>

<style scoped>

</style>