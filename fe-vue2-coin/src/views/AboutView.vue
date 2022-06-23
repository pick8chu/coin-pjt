<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>
<script>
export default {
name: "aboutView",
data() {
},
mounted() {
  this.getLatestData()
},
methods: {
    getLatestData(){
        this.$axios.get(`/r/FIhqL`)
        .then((res)=>{
            this.quoteList = res.data
        })
    }
},

}
</script>

<style>

</style>