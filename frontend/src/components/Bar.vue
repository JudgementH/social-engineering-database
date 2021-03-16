<template>
    <div>
        <v-app-bar
                color="green"
                dense
        >
            <div class="white--text">
                <v-toolbar-title>社工库</v-toolbar-title>
            </div>

            <template>
                <v-tabs
                        align-with-title
                        dark
                        color="white"
                >
                    <v-tabs-slider color="white"/>
                    <v-tab @click="toQQGroupSearch">QQ群查询</v-tab>
                    <v-tab @click="toHelloWorld">Hello World</v-tab>
                </v-tabs>
            </template>


            <v-spacer/>

            <v-btn icon>
                <v-icon>mdi-heart</v-icon>
            </v-btn>
            <v-menu
                    open-on-hover
                    offset-y
                    bottom
                    transition="slide-y-transition"
            >
                <template v-slot:activator="{ on, attrs }">
                    <v-btn
                            icon
                            v-bind="attrs"
                            v-on="on"
                    >
                        <v-icon>mdi-dots-vertical</v-icon>
                    </v-btn>
                </template>

                <v-list>
                    <v-list-item
                            v-for="(item, index) in lists"
                            :key="index"
                    >
                        <v-list-item-title>{{ item }}</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>

        </v-app-bar>

    </div>
</template>

<script>
    export default {
        name: "Bar",
        data: () => ({
            lists: [
                '社工库',
                'Judgement',
            ],
        }),
        methods: {
            toQQGroupSearch() {
                this.$router.push({path: './'})
            },
            toHelloWorld() {
                this.$router.push({path: './helloworld'})
            }
        }
    }
</script>

<style scoped>

</style>