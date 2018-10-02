<template>
    <edit-form  url="/pricing/product"
                :title="title"
                :pk="pk"
                :csrftoken="csrftoken"
                :cols="cols"
                :init_form="form">
    </edit-form>
</template>

<script>
import EditFrom from 'components/EditForm.vue'
export default {
    props: {
        context: Object
    },
    data: function() {
        return {
            csrftoken: String,
            pk: Number,
            form: Array,
        }
    },
    components: {
        'edit-form': EditFrom
    },
    data: function() {
        return {
            title: 'Nowy produkt',
            cols: {
                name: {display: 'Imie', type: 'text'},
                surname: {display: 'Nazwisko', type: 'text'},
                age: {display: 'Wiek', type: 'number'},
            }
        }
    },
    created: function() {
        console.log(this.context)
        this.csrftoken = this.context['csrftoken'];
        this.pk = this.context['pk'];
        this.form = this.context['init_form'];
        console.log(this.form)

        if(this.pk)
            this.title = 'Edytuj uzytkownika (id:' + this.pk + ')';
    },
}
</script>

