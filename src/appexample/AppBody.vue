<template>
    <example-body active_app='appexample'>
        <template slot="navigation">
            <navigation :items="items" :active_item="active_item">
            </navigation>
        </template>
        <slot></slot>
    </example-body>
</template>

<script>
import ExampleBody from '../ExampleBody.vue'
import AppNavigation from 'components/AppNavigation.vue'
export default {
    props: {
        active_item: String
    },
    components: {
        'example-body': ExampleBody,
        'navigation': AppNavigation
    },
    data: function() {
        return {
            items: [
                {name: 'user_new', display: 'Dodaj użytkownika', href: '/appexample/user/new'},
                {name: 'user_list', display: 'Lista użytkowników', href: '/appexample/users'},
            ]
        }
    }
}
</script>
