<template>
    <div>
      <div class="d-flex ml-5 mr-5">
            <div class="w-500px input-group">
                <span class="input-group-text">symbol to currency</span>
                <input v-model="symbols" type="text" class="form-control" placeholder="symbol">
                <span class="input-group-text">to</span>
                <input v-model="currencys" type="text" class="form-control" placeholder="currency">
            </div>
            <from-to-datepicker @change="(_date) => {date = _date}"/>
            <div class="">
                <b-button @click="getHistoryData"> get history data </b-button>
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
import FromToDatepicker from '@/components/from-to-datepicker.vue'

export default {
name: "SearchHistoryData",
components: {
    FromToDatepicker
},
data() {
    return {
        symbols: "BTC,ETH",
        currencys: "KRW",
        quoteList: "",
        date: {},
    }
},
methods: {
    getHistoryData(){
        this.$axios.get(`/quote-history/${this.symbols}`, {
            params: {
                currencys: this.currencys,
                dateFrom: this.date.from,
                dateTo: this.date.to
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
.w-500px{
    width:500px !important
}
.w-700px{
    width:700px !important
}
</style>