<template>
  <div class="projectoverview">
    <h1 class="title">当前进行中项目 {{projectLength}} 个</h1>
    <div class="highcharts row_top">
      <div id="collection" ref="collection" style="width: 400px; height: 300px;">123456</div>
      <div id="consume" style="width: 400px; height: 300px;"></div>
      <div id="monthlyknot" style="width: 400px; height: 300px;"></div>
    </div>
    <h1 class="title">每日项目数据</h1>
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.results" style="width: 100%" header-align="center">
          <el-table-column label="日期" prop="date"></el-table-column>
          <el-table-column label="在线项目数" prop="start_num"></el-table-column>
          <el-table-column label="结项项目数" prop="finish_num"></el-table-column>
          <el-table-column label="投资人数" prop="invest_count"></el-table-column>
          <el-table-column label="投资金额" prop="invest_amount"></el-table-column>
          <el-table-column label="预估消耗费用" prop="consume_amount"></el-table-column>
          <el-table-column label="返现人数" prop="return_count"></el-table-column>
          <el-table-column label="返现投资金额" prop="return_invest_amount"></el-table-column>
          <el-table-column label="返现费用" prop="return_amount"></el-table-column>
        </el-table>
      </div>
      <div class="pagination">
        <el-pagination
          background
          @current-change="handleCurrentChange"
          :page-size="10"
          :current-page="this.currentPage"
          layout="prev, pager, next, total, jumper"
          :total="this.dataList.recordCount">
        </el-pagination>
      </div>
    </el-row>
  </div>
</template>

<script>
import Highcharts from 'highcharts'
import {getProjectOver, getAllProject} from '@/api/api'

export default {
  data () {
    return {
      dataarr: [
        ['Firefox', 12345],
        ['IE', 0],
        ['Chrome', 0]
      ],
      dataList: [],
      currentPage: 1,
      loading: true,
      pie_data_1: [],
      pie_data_2: [],
      pie_data_3: [],
      num_detail_1: [],
      num_detail_2: [],
      num_detail_3: [],
      projectLength: 0
    }
  },
  created () {
    this.getDatalist()
  },
  mounted () {
    /* this.charts('monthlyknot', this.dataarr, '当月结项项目分布') */
    this.getProjectdata()
    this.getProjectdata2()
  },
  methods: {
    getDatalist () {
      getProjectOver(this.currentPage).then((res) => {
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
      this.getDatalist()
    },
    charts (dom, datas, titles, name) {
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
          name: name,
          data: datas
        }]
      })
    },
    getProjectdata () {
      let data = {
        params: {
          page: 1,
          pageSize: 999,
          state: 1
        }
      }
      getAllProject(data).then((res) => {
        if (res.data.code === 0) {
          let data = res.data.results
          for (var i = 0; i < data.length; i++) {
            if (data[i].consume >= 0) {
              this.pie_data_1.push([data[i].name, parseFloat(data[i].consume)])
              this.num_detail_1 += parseFloat(data[i].consume)
            } else {
              this.pie_data_2.push([data[i].name, parseFloat(data[i].consume)])
              this.num_detail_2 += parseFloat(data[i].consume)
            }
            this.projectLength++
          }
          this.charts('collection', this.pie_data_1, '项目预估待收布图', '预估待收')
          this.charts('consume', this.pie_data_2, '项目预估待消耗分布', '预估待消耗')
        } else {
          /* this.$message(res.data.detail) */
        }
      }).catch((err) => {
        console.log(err)
      })
    },
    getProjectdata2 () {
      let dateNow = new Date()
      let m = (dateNow.getMonth() + 1) < 10 ? '0' + (dateNow.getMonth() + 1) : dateNow.getMonth() + 1
      let dateStr = `${dateNow.getFullYear()}-${m}-01`
      let data2 = {
        params: {
          page: 1,
          pageSize: 999,
          state: 5,
          concluded_audit_date_0: dateStr
        }
      }
      getAllProject(data2).then((res) => {
        if (res.data.code === 0) {
          let data = res.data.results
          for (var i = 0; i < data.length; i++) {
            this.pie_data_3.push([data[i].name, parseFloat(data[i].settle)])
            this.num_detail_3 += parseFloat(data[i].settle)
          }
          this.charts('monthlyknot', this.pie_data_3, '当月结项项目分布', '结算费用')
        } else {
          /* this.$message(res.data.detail) */
        }
      }).catch((err) => {
        console.log(err)
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
