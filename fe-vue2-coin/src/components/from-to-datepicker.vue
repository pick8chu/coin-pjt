<template>
    <div class="d-flex justify-content-between">
        <div class="datepicker-box d-flex justify-content-between">
            <b-form-datepicker
                class="w-180px"
                variant="primary"
                locale='en-US'
                today-button
                reset-button
                v-model="date.from"
                label-no-date-selected="from"
                hide-header
                :max="date.to"
                :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                @input="inputChanged"/>
            <b-form-datepicker
                class="w-180px"
                variant="primary"
                locale='en-US'
                dropleft
                today-button
                reset-button
                v-model="date.to"
                label-no-date-selected="to"
                hide-header
                :min="date.from"
                :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                @input="inputChanged"/>
        </div>
    </div>
</template>


<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
    props: {
    },
    data() {
        return {
            date: {
                from: "",
                to: "",
            }
        }
    },
    computed: {
    },
    methods: {
        inputChanged () {
            this.$emit("change", this.date);
        },
    }
})
</script>

<style>
.w-180px{
    width:180px !important
}
</style>