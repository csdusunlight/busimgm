<template>
  <div class="dataOverview">
    <el-row class="row_bottom">
      <el-row class="row_line-height">
        <h1 class="title">个人项目总览</h1>
        <div class="table-list">
          <el-table v-loading="loading" :data="projectOverview.results" style="width: 100%">
            <el-table-column label="在线项目数" prop="online_num"></el-table-column>
            <el-table-column label="待结算金额" prop="to_settle_amount"></el-table-column>
            <el-table-column label="待结算项目数" prop="to_settle_num"></el-table-column>
            <el-table-column label="待消耗金额" prop="to_consume_amount"></el-table-column>
            <el-table-column label="待消耗项目数" prop="to_consume_num"></el-table-column>
          </el-table>
        </div>
      </el-row>
      <el-row>
        <h1 class="title">每日项目数据</h1>
        <div class="table-list">
          <el-table v-loading="loadingproject" :data="dataList.results" style="width: 100%">
            <el-table-column label="日期" prop="date"></el-table-column>
            <el-table-column label="新增项目数" prop="start_num"></el-table-column>
            <el-table-column label="结项项目数" prop="finish_num"></el-table-column>
            <el-table-column label="投资人数" prop="invest_count"></el-table-column>
            <el-table-column label="投资金额" prop="invest_amount"></el-table-column>
            <el-table-column label="消耗费用" prop="consume_amount"></el-table-column>
            <el-table-column label="返现投资人数" prop="return_count"></el-table-column>
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
    </el-row>
  </div>
</template>

<script>
import {getDataOverview, getDataDayList} from '@/api/api'
import {mapGetters} from 'vuex'
export default {
  data () {
    return {
      dataList: [],
      loading: true,
      dialogVisible: false,
      currentPage: 1,
      projectOverview: {}
    }
  },
  created () {
    this.getDataAllList()
    this.getDayDataList()
  },
  methods: {
    /* 获取项目总览 */
    getDataAllList () {
      setTimeout(() => {
        let data = this.conditionDate()
        getDataOverview(data).then((res) => {
          console.log(res.data)
          if (res.data.code === 0) {
            this.projectOverview = res.data
            this.loading = false
          }
        }).catch((err) => {
          console.log(err)
        })
      }, 300)
    },
    /* 获取每日项目数据 */
    getDayDataList () {
      setTimeout(() => {
        let data = this.conditionDate()
        getDataDayList(this.currentPage, data).then((res) => {
          console.log(res)
          this.dataList = res.data
          this.loadingproject = false
        }).catch((err) => {
          console.log(err)
        })
      }, 300)
    },
    /* 搜索条件拼接 */
    conditionDate () {
      let Data = {
        params: {
          user: this.userId
        }
      }
      return Data
    },
    /* 分页 */
    handleCurrentChange (val) {
      this.datalist = []
      this.loading = true
      this.currentPage = val
      this.getDayDataList()
    }
  },
  computed: {
    ...mapGetters([
      'userId'
    ])
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.dataOverview
  .el-tabs__content
    padding-top: 30px;
    padding-bottom: 40px;
  .row_line-height
    margin-bottom: 70px;
</style>
