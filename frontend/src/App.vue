<script>

</script>
<template>
    <q-layout view="hHh lpR fFf">

        <q-header reveal elevated class="bg-primary text-white">
            <q-toolbar>
                <q-toolbar-title>
                    CHendLess
                </q-toolbar-title>
            </q-toolbar>
        </q-header>

        <q-page-container>
            <router-view/>
        </q-page-container>

        <q-footer bordered class="bg-grey-8 text-white">
            <q-toolbar>
                <q-toolbar-title>
                    <div class="absolute-center">Impressum</div>
                </q-toolbar-title>
            </q-toolbar>
        </q-footer>

    </q-layout>
</template>

<style>
</style>