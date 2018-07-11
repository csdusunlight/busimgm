<template>
  <div class="dataOverview">
    <el-row class="row_bottom">
      <el-row class="row_line-height">
        <h1 class="title">项目总览</h1>
        <div class="table-list">
          <el-table v-loading="loading" :data="projectOverview.data" style="width: 100%">
            <el-table-column label="在线项目数" prop="onlineprojectnum"></el-table-column>
            <el-table-column label="待结算金额" prop="currenttosettlenum"></el-table-column>
            <el-table-column label="待结算项目数" prop="currenttosettlepronum"></el-table-column>
            <el-table-column label="待消耗金额" prop="currenttoconsumenum"></el-table-column>
            <el-table-column label="待消耗项目数" prop="currenttoconsumepronum"></el-table-column>
          </el-table>
        </div>
      </el-row>
      <el-row>
        <h1 class="title">每日项目数据</h1>
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
    </el-row>
  </div>
</template>

<script>
import {getDataOverview} from '@/api/api'

export default {
  data () {
    return {
      dataList: [],
      loading: true,
      dialogVisible: false,
      currentPage: 1,
      projectOverview: {
        data: [
          {
            currenttoconsumenum: '',
            currenttoconsumepronum: '',
            currenttosettlenum: '',
            currenttosettlepronum: '',
            onlineprojectnum: ''
          }
        ]
      }
    }
  },
  created () {
    this.getDatalist()
  },
  methods: {
    /* 获取项目总览 */
    getDatalist () {
      getDataOverview().then((res) => {
        console.log(res)
        console.log(res.data.data['currenttoconsumenum'])
        this.projectOverview.data[0].currenttoconsumenum = res.data.data['currenttoconsumenum']
        this.projectOverview.data[0].currenttoconsumepronum = res.data.data['currenttoconsumepronum']
        this.projectOverview.data[0].currenttosettlenum = res.data.data['currenttosettlenum']
        this.projectOverview.data[0].currenttosettlepronum = res.data.data['currenttosettlepronum']
        this.projectOverview.data[0].onlineprojectnum = res.data.data['onlineprojectnum']
        console.log(this.projectOverview.data)
        this.loading = false
      }).catch((err) => {
        console.log(err)
      })
    },
    /* 分页 */
    handleCurrentChange (val) {
      this.datalist = []
      this.loading = true
      this.currentPage = val
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
  .row_line-height
    margin-bottom: 70px;
</style>
