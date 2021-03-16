<template>
    <div>
        <div>
            <v-row
                    justify="center"
                    class="green text-center"
                    style="padding-top: 100px;"
            >
                <v-col cols="6" align-self="center">
                    <div class="text-xl-h2 white--text py-8">QQ群社工库查询</div>
                    <div class="white--text py-sm-10">查询qq号加入的QQ群，和QQ群内成员信息</div>
                </v-col>
            </v-row>
            <v-row
                    justify="center"
                    class="green text-center">
                <v-col cols="1">
                    <v-select
                            :items="selectItem"
                            outlined
                            label="类别"
                            color="black"
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
                                color="black"
                                v-model="searchText"
                                @click:prepend-inner="click"
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
        {{test}}
    </div>

</template>

<script>
    export default {
        name: "QQGroupSearch",
        data() {
            return {
                selectItem: ['qq号', 'qq群号'],
                test:"",
                searchLabel: "",
                searchText: "",
                page: 1,
                pageCount: 0,
                itemsPerPage: 5,
                headers: [
                    {
                        text: 'Dessert (100g serving)',
                        align: 'start',
                        sortable: false,
                        value: 'name',
                    },
                    {text: 'Calories', value: 'calories'},
                    {text: 'Fat (g)', value: 'fat'},
                    {text: 'Carbs (g)', value: 'carbs'},
                    {text: 'Protein (g)', value: 'protein'},
                    {text: 'Iron (%)', value: 'iron'},
                ],
                desserts: [
                    {
                        name: 'Frozen Yogurt',
                        calories: 159,
                        fat: 6.0,
                        carbs: 24,
                        protein: 4.0,
                        iron: '1%',
                    },
                    {
                        name: 'Ice cream sandwich',
                        calories: 237,
                        fat: 9.0,
                        carbs: 37,
                        protein: 4.3,
                        iron: '1%',
                    },
                    {
                        name: 'Eclair',
                        calories: 262,
                        fat: 16.0,
                        carbs: 23,
                        protein: 6.0,
                        iron: '7%',
                    },
                    {
                        name: 'Cupcake',
                        calories: 305,
                        fat: 3.7,
                        carbs: 67,
                        protein: 4.3,
                        iron: '8%',
                    },
                    {
                        name: 'Gingerbread',
                        calories: 356,
                        fat: 16.0,
                        carbs: 49,
                        protein: 3.9,
                        iron: '16%',
                    },
                    {
                        name: 'Jelly bean',
                        calories: 375,
                        fat: 0.0,
                        carbs: 94,
                        protein: 0.0,
                        iron: '0%',
                    },
                    {
                        name: 'Lollipop',
                        calories: 392,
                        fat: 0.2,
                        carbs: 98,
                        protein: 0,
                        iron: '2%',
                    },
                    {
                        name: 'Honeycomb',
                        calories: 408,
                        fat: 3.2,
                        carbs: 87,
                        protein: 6.5,
                        iron: '45%',
                    },
                    {
                        name: 'Donut',
                        calories: 452,
                        fat: 25.0,
                        carbs: 51,
                        protein: 4.9,
                        iron: '22%',
                    },
                    {
                        name: 'KitKat',
                        calories: 518,
                        fat: 26.0,
                        carbs: 65,
                        protein: 7,
                        iron: '6%',
                    },
                ],
            }
        },
        methods:{
            click(){
                this.searchText = "213"
            },
            sendMessage(){
                this.test = "1111"
            }
        }
    }
</script>

<style scoped>

</style>