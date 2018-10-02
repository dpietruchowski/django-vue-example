<template>
    <div>
        <navigation name="Django Vue Example" :apps="apps" :active_app="active_app">
        </navigation>
        <div class="container-fluid">
            <div class="row">   
                <slot name="navigation"></slot>
                <main role="main" class="col-sm-9 col-md-10">
                    <slot></slot>
                </main><!-- /.container -->
            </div>
        </div>
    </div>
</template>

<script>
import Navigation from 'components/Navigation.vue'
export default {
    props: {
        active_app: String
    },
    components: {
        'navigation': Navigation
    },
    data: function() {
        return {
            apps: [
                {name: 'appexample', display: 'App example',  href: '/appexample'}
            ],
        }
    }
}
</script>

<style>
  body {
    padding-top: 70px;
  }
</style>

