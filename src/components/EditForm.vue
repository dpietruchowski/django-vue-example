<template>
    <div class="card bg-light mx-auto">
      <div class="text-center">
        <form method="POST" :id="get_formid()" class="post-form" @submit="save">
          <input type="hidden" name="csrfmiddlewaretoken" :value="csrftoken" />
          <div class="card-body">
            <h4 class="card-title">{{ title }}</h4>
          </div>
          <div v-for="(col, col_name) in cols" class="card-body">
            <div style="float:left;"><p class="card-text" >{{ col.display }}</p></div>
            <div style="float:right;">
                <p class="card-text" >
                    <input v-if="get_type(col) == 0" :type="col.type" :name="col_name" maxlength="30" required :id="'id_' + col_name" v-model="col.value"/>
                    <select v-if="get_type(col) == 1" :name="col_name" :id="'id_' + col_name" v-model="col.value">  
                        <option selected disabled>Wybierz</option>
                        <option v-for="option in col.options" :value="option.value">{{ option.display }}</option>
                    </select>
                    <textarea v-if="get_type(col) == 2" :name="col_name" cols="40" rows="10" required="" :id="get_id(col_name)" style="height: 231px;" v-model="col.value"></textarea>
                </p>
            </div>
          </div>
          <div class="card-body">
            <slot></slot>
          </div>
          <div class="card-body">
            <button type="submit" class="save btn btn-default">Zapisz</button>
            <button v-if="pk" type="button" class="save btn btn-default" @click="delete_object">Usuń</button>
          </div>
        </form>
      </div>
    </div>
</template>

<script>
export default {
    props: {
        form_id: {
            default: 0,
            type: Number,
        },
        url: String,
        title: String,
        pk: Number,
        csrftoken: String,
        cols: Object,
        init_form: Array,
        async: Boolean
    },
    data: function() {
        return {
        }
    },
    methods: {
        delete_object: function() {
            fetch(this.url + '/edit/' + this.pk, {
                method: 'DELETE',
                credentials: "same-origin",
                headers: {
                    "X-CSRFToken": this.csrftoken,
                },
            })
            .then(resp => resp.json())
            .then(resp => {
                console.log(resp);
                location.href=this.url + 's';
            })
        },

        save: function(e) {
            if (!this.async)
                return true;
            e.preventDefault();
            var data = new URLSearchParams();
            var formElement = document.querySelector('#' + this.get_formid());
            for(var pair of new FormData(formElement)) {
                data.append(pair[0], pair[1]);
            }
            if (this.pk)
                var url = this.url + '/edit/' + this.pk;
            else
                var url = this.url + '/new';
            fetch(url, {
                method: 'POST',
                body: data,
                credentials: "same-origin",
                headers: {
                    "X-CSRFToken": this.csrftoken,
                    'X-Requested-With': 'XMLHttpRequest'
                },
            })
            .then(resp => resp.json())
            .then(resp => {
                this.$emit('saved', resp.object.fields);
                console.log(resp);
                alert(resp.result);
            });
            return false;
        },
        get_type: function(col) {
            if(col.type == 'select') return 1
            if(col.type == 'textarea') return 2
            return 0
        },
        get_id: function(col_name) {
            return 'id' + col_name;
        },
        get_formid: function() {
            return 'form' + this.form_id;
        }
    },
    created: function() {
        if(this.init_form) {
            const fields = this.init_form[0];
            console.log(JSON.stringify(this.init_form))
            Object.keys(fields).forEach(function(key, index) {
                this.cols[key].value = fields[key];
            }, this);
        }
    },
}
</script>

