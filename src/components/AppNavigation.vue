<template>
    <nav class="col-md-2 d-none d-md-block bg-light sidebar">
        <div class="sidebar-sticky">
            <ul class="nav flex-column">
                <li v-for="item in items" class="nav-item">
                    <a class="nav-link p-2" :class="{ active : active_item === item.name }" :href="item.href">{{ item.display }}</a>
                </li> 
            </ul>
        </div>
    </nav>
</template>

<script>
export default {
    props: {
        items: Array,
        active_item: String
    },
}
</script>