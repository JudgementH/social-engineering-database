<template>
    <v-app app>
        <Bar/>
        <v-main>
            <v-container fluid><!-- 如果使用vue-router -->
                <router-view></router-view>
            </v-container>
        </v-main>
        <Footer/>
    </v-app>
</template>

<script>
    import Bar from "./components/Bar";
    import Footer from "./components/Footer";

    export default {
        name: 'App',

        components: {
            Footer,
            Bar,
        },

        data: () => ({
            //
        }),
    };
</script>
