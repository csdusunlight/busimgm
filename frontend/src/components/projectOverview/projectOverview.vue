<template>
  <div class="projectoverview">
    <div class="highcharts">
      <div id="collection" ref="collection" style="width: 400px; height: 300px;">123456</div>
      <div id="consume"></div>
      <div id="monthlyknot"></div>
    </div>
  </div>
</template>

<script>
import Highcharts from 'highcharts'

export default {
  data () {
    return {
      dataarr: [
        ['Firefox', 45.0],
        ['IE', 26.8],
        ['Chrome', 12.8],
        ['Safari', 8.5],
        ['Opera', 6.2],
        ['其他', 0.7]
      ]
    }
  },
  mounted () {
    this.collectionfun()
  },
  methods: {
    collectionfun () {
      let that = this
      Highcharts.chart('collection', {
        title: {
          text: '项目预估待收分布'
        },
        credits: {
          enabled: false
        },
        plotOptions: {
          pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
              enabled: true,
              format: '<b>{point.name}</b>: {point.percentage:.1f} %',
              style: {
                color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
              }
            }
          }
        },
        series: [{
          type: 'pie',
          name: '浏览器访问占比',
          data: that.dataarr
        }]
      })
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
</style>
