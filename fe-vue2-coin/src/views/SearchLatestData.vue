<template>
    <div>
      <div class="d-flex ml-5 mr-5">
            <div class="input-group">
                <span class="input-group-text">symbol to currency</span>
                <input v-model="symbols" type="text" class="form-control" placeholder="symbol">
                <span class="input-group-text">to</span>
                <input v-model="currencys" type="text" class="form-control" placeholder="currency">
            </div>
            <div class="w-25">
                <b-button @click="getLatestData"> get latest data </b-button>
            </div>
        </div>
        <div v-if="quoteList">
            <table class="table">
                <thead>
                    <tr>
                        <th scope="col">symbol</th>
                        <th scope="col">name</th>
                        <th scope="col">currency</th>
                        <th scope="col">timestamp</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in quoteList" :key="item.cid">
                        <td>{{item.symbol}}</td>
                        <td>{{item.name}}</td>
                        <td>{{`${item.price} ${item.currency}`}}</td>
                        <td>{{item.last_updated}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>  
</template>

<script>
export default {
name: "SearchLatestData",
data() {
    return {
        symbols: "BTC,ETH",
        currencys: "KRW",
        quoteList: "",
    }
},
methods: {
    getLatestData(){
        this.$axios.get(`/quotes/${this.symbols}`, {
            params: {
                currencys: this.currencys
            }
        })
        .then((res)=>{
            this.quoteList = res.data
        })
    }
},

}
</script>

<style>

</style>