<template>
  <div class="dataOverview">
    <el-row class="row_bottom">
      <el-tabs type="border-card" class="card">
        <el-tab-pane label="项目总览">
          <el-row>
            <div class="table-list">
              <el-table v-loading="loading" :data="dataList.data" style="width: 100%">
                <el-table-column label="在线项目数" prop="integer"></el-table-column>
                <el-table-column label="待结算金额" prop="string"></el-table-column>
                <el-table-column label="待结算项目数" prop="integer"></el-table-column>
                <el-table-column label="待消耗金额" prop="integer"></el-table-column>
                <el-table-column label="待消耗项目数" prop="qq_number"></el-table-column>
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
        </el-tab-pane>
        <el-tab-pane label="每日项目数据">
          <el-row>
            <div class="table-list">
              <el-table v-loading="loading" :data="dataList.data" style="width: 100%">
                <el-table-column label="日期" prop="date"></el-table-column>
                <el-table-column label="新增项目数" prop="string"></el-table-column>
                <el-table-column label="结项项目数" prop="integer"></el-table-column>
                <el-table-column label="有效项目数" prop="integer"></el-table-column>
                <el-table-column label="投资人数" prop="qq_number"></el-table-column>
                <el-table-column label="投资金额" prop="float"></el-table-column>
                <el-table-column label="消耗费用" prop="integer"></el-table-column>
                <el-table-column label="返现投资人数" prop="integer"></el-table-column>
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
        </el-tab-pane>
      </el-tabs>
    </el-row>
  </div>
</template>

<script>
import {dataPage} from '@/api/api'

export default {
  data () {
    return {
      dataList: [],
      loading: true,
      dialogVisible: false,
      currentPage: 1,
      param: {
        page: 1
      }
    }
  },
  created () {
    this.getDatalist()
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
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.dataOverview
  .el-tabs__content
    padding-top: 30px;
    padding-bottom: 40px;
</style>
