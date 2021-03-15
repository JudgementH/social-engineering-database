<template>
    <v-footer
            dark
            padless
    >
        <v-card
                class="flex"
                flat
                tile
        >
            <v-card-text class="green white--text text-center">
                <strong class="subheading">仅仅用于系统安全的学习</strong>
            </v-card-text>

            <v-card-text class="py-2 white--text text-center">
                Copyright © {{ new Date().getFullYear() }} Judgement. All rights reserved.
            </v-card-text>
        </v-card>
    </v-footer>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>

</style>