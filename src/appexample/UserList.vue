<template>
    <app-body active_item="user_list">
        <search-list edit title="Lista użytkowników"
                    url="/appexample/user"
                    :cols="cols">

        </search-list>
    </app-body>
</template>

<script>
import SearchList from 'components/SearchList.vue'
import AppBody from './AppBody.vue'
export default {
    components: {
        'search-list': SearchList,
        'app-body': AppBody
    },
    data: function() {
        return {
            cols: [
                {name: 'id', display: 'Id'},
                {name: 'name', display: 'Imie'},
                {name: 'surname', display: 'Nazwiskow'},
                {name: 'age', display: 'Wiek'},
            ]
        }
    }
}
</script>