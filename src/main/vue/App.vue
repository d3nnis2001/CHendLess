<script setup>
import {ref} from 'vue'

const leftDrawerOpen = ref(false)

function toggleLeftDrawer() {
    leftDrawerOpen.value = !leftDrawerOpen.value
}
</script>
<template>
    <q-layout view="hHh lpR fFf">

        <q-header reveal elevated class="bg-primary text-white">
            <q-toolbar>
                <q-btn dense flat round icon="menu" @click="toggleLeftDrawer"/>
                <q-toolbar-title>
                    CHendLess
                </q-toolbar-title>
            </q-toolbar>
        </q-header>

        <q-drawer show-if-above v-model="leftDrawerOpen" side="left" bordered>
            <q-list>
                <q-item clickable>
                    <q-item-section avatar>
                        <q-icon name="newspaper"/>
                    </q-item-section>
                    <q-item-section>
                        <router-link to="/">Übersicht</router-link>
                    </q-item-section>
                </q-item>
                <q-item clickable>
                    <q-item-section avatar>
                        <q-icon name="library_add"/>
                    </q-item-section>
                    <q-item-section>
                        <router-link to="/create">Neuer Artikel</router-link>
                    </q-item-section>
                </q-item>
                <q-item  @click="" clickable>
                    <q-item-section avatar>
                        <q-icon name="logout"/>
                    </q-item-section>
                    <q-item-section>
                        Logout
                    </q-item-section>
                </q-item>
                <q-item clickable>
                    <q-item-section avatar>
                        <q-icon name="login"/>
                    </q-item-section>
                    <q-item-section>
                        <router-link to="/login">Login</router-link>
                    </q-item-section>
                </q-item>
            </q-list>
        </q-drawer>

        <q-page-container>
            <router-view/>
        </q-page-container>

        <q-footer bordered class="bg-grey-8 text-white">
            <q-toolbar>
                <q-toolbar-title>
                    <div>GPSE</div>
                </q-toolbar-title>
            </q-toolbar>
        </q-footer>

    </q-layout>
</template>

<style scoped>
</style>
