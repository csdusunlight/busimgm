<template>
  <div class="projectoverview">
    <h1 class="title">当前在线项目1000</h1>
    <div class="highcharts row_top">
      <div id="collection" ref="collection" style="width: 400px; height: 300px;">123456</div>
      <div id="consume" style="width: 400px; height: 300px;"></div>
      <div id="monthlyknot" style="width: 400px; height: 300px;"></div>
    </div>
    <h1 class="title">每日项目数据</h1>
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.data" style="width: 100%" header-align="center">
          <el-table-column label="日期" prop="date"></el-table-column>
          <el-table-column label="在线项目数" prop="integer"></el-table-column>
          <el-table-column label="结项项目数" prop="integer"></el-table-column>
          <el-table-column label="投资人数" prop="integer"></el-table-column>
          <el-table-column label="投资金额" prop="integer"></el-table-column>
          <el-table-column label="预估消耗费用" prop="integer"></el-table-column>
          <el-table-column label="返现人数" prop="integer"></el-table-column>
          <el-table-column label="返现投资金额" prop="integer"></el-table-column>
          <el-table-column label="返现费用" prop="integer"></el-table-column>
        </el-table>
      </div>
      <div class="pagination">
        <el-pagination
          background
          @current-change="handleCurrentChange"
          :page-size="10"
          :current-page="this.currentPage"
          layout="prev, pager, next, total, jumper"
          :total="this.dataList.total">
        </el-pagination>
      </div>
    </el-row>
  </div>
</template>

<script>
import Highcharts from 'highcharts'
import {dataPage} from '@/api/api'

export default {
  data () {
    return {
      dataarr: [
        ['Firefox', 12345],
        ['IE', 456456],
        ['Chrome', 7897946],
        ['Safari', 12313],
        ['Opera', 45646],
        ['其他', 45646],
        ['Firefox', 12345],
        ['IE', 456456],
        ['Chrome', 7897946],
        ['Safari', 12313],
        ['Opera', 45646],
        ['其他', 45646],
        ['Firefox', 12345],
        ['IE', 456456],
        ['Chrome', 7897946],
        ['Safari', 12313],
        ['Opera', 45646],
        ['其他', 45646],
        ['Firefox', 12345],
        ['IE', 456456],
        ['Chrome', 7897946],
        ['Safari', 12313],
        ['Opera', 45646],
        ['其他', 45646]
      ],
      dataList: [],
      currentPage: 1,
      loading: true,
      param: {
        page: 1
      }
    }
  },
  created () {
    this.getDatalist()
  },
  mounted () {
    this.charts('collection', this.dataarr, '项目预估待收布图')
    this.charts('consume', this.dataarr, '项目预估待消耗分布')
    this.charts('monthlyknot', this.dataarr, '当月结项项目分布')
  },
  methods: {
    getDatalist () {
      dataPage(this.param).then((res) => {
        console.log(res)
        this.dataList = res.data
        this.loading = false
      }).catch((err) => {
        console.log(err)
      })
    },
    handleCurrentChange (val) {
      this.datalist = []
      this.loading = true
      this.currentPage = val
      this.param.page = val
      this.getDatalist()
    },
    charts (dom, datas, titles) {
      Highcharts.chart(dom, {
        title: {
          text: titles
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
              format: '<b>{point.name}</b>: {point.y}',
              style: {
                color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
              }
            }
          }
        },
        series: [{
          type: 'pie',
          name: '浏览器访问占比',
          data: datas
        }]
      })
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.projectoverview
  .title
    font-weight: normal;
    font-size: 18px;
.highcharts
  display: flex;
  justify-content: space-between;
  align-items: center;
</style>
