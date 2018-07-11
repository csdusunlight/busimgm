<template>
  <div class="projectLive">
    <el-row >
      <el-col :span="24">
        <div class="input_search">
          <div class="search">
            <label class="labeltext">立项日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate0" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> —— </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate1" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
          <div class="search">
            <label class="labeltext">项目编号</label>
            <el-input size="medium" v-model="projectnum"></el-input>
          </div>
          <div class="search">
            <label class="labeltext">项目名称</label>
            <el-input size="medium" v-model="projectname"></el-input>
          </div>
          <div class="select">
            <label class="label">项目状态</label>
            <el-select size="medium" v-model="selectvalue" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="4" :offset="20">
        <div class="flexright">
          <el-button size="medium" type="primary">搜索</el-button>
          <el-button size="medium" type="info">导出</el-button>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.results" style="width: 100%" @row-click="handleRowHandle">
          <el-table-column label="项目编号" prop="id"></el-table-column>
          <el-table-column label="项目名称" prop="name"></el-table-column>
          <el-table-column label="立项日期" prop="lanched_audit_date"></el-table-column>
          <el-table-column label="结项日期" prop="concluded_audit_date"></el-table-column>
          <el-table-column label="预计待收/待消耗" prop="topay_amount"></el-table-column>
          <el-table-column label="预计总消耗" prop="consume"></el-table-column>
          <el-table-column label="总返现金额" prop="cost"></el-table-column>
          <el-table-column label="项目状态" prop="state"></el-table-column>
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
      <el-dialog title="项目数据" :visible.sync="lookProjectTable" width="70%">
        <div class="table-list">
          <el-table :data="detailsList.results" style="width: 100%" @row-click='handleRowHandle'>
            <el-table-column label="日期" prop="date"></el-table-column>
            <el-table-column label="项目名称" prop="1"></el-table-column>
            <el-table-column label="投资人数" prop="1"></el-table-column>
            <el-table-column label="投资金额" prop="invest_amount"></el-table-column>
            <el-table-column label="消耗费用" prop="consume_amount"></el-table-column>
            <el-table-column label="返现投资人数" prop="1" width="95"></el-table-column>
            <el-table-column label="返现投资金额" prop="1"></el-table-column>
            <el-table-column label="返现费用" prop="return_amount"></el-table-column>
          </el-table>
        </div>
        <div class="pagination">
          <el-pagination
            background
            @current-change="detailsCurrentChange"
            :page-size="10"
            :current-page="this.detailsCurrentPage"
            layout="prev, pager, next, total, jumper"
            :total="this.detailsList.recordCount">
          </el-pagination>
        </div>
      </el-dialog>
    </el-row>
  </div>
</template>

<script>
import {getProjectLive, getprojectDetails} from '@/api/api'
export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      projectnum: '',
      projectname: '',
      selectvalue: '0',
      loading: true,
      currentPage: 1,
      searchDetailsName: '',
      lookProjectTable: false,
      detailsList: {},
      dataList: {},
      options: [
        {
          value: '0',
          label: '全部'
        },
        {
          value: '1',
          label: '进行中'
        },
        {
          value: '4',
          label: '结项中'
        },
        {
          value: '5',
          label: '已结项'
        },
        {
          value: '6',
          label: '结项失败'
        }
      ]
    }
  },
  created () {
    this.getProjectList()
  },
  methods: {
    getProjectList () {
      let data = this.conditionDate()
      getProjectLive(this.currentPage, data).then((res) => {
        console.log(res)
        this.dataList = res.data
        this.loading = false
      }).catch((err) => {
        console.log('error')
        console.log(err)
      })
    },
    conditionDate () {
      let Data = {
        params: {
          state: this.selectvalue
        }
      }
      return Data
    },
    /* 分页 */
    handleCurrentChange (val) {
      this.loading = true
      this.currentPage = val
      this.getProjectList()
    },
    /* 点击 行 查看详情 */
    handleRowHandle (val) {
      console.log(val)
      this.searchDetailsName = val.id
      this.lookProjectTable = true
      this.getDetailsList()
    },
    /* 单击行详情搜索 */
    getDetailsList () {
      let data = {
        params: {
          project: this.searchDetailsName
        }
      }
      getprojectDetails(this.detailsCurrentPage, data).then((res) => {
        console.log(res)
        this.detailsList = res.data
      })
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.projectLive
  .flexright
    display: flex;
    justify-content: flex-end;
  .select
    .label
      margin-right: 10px;
  .row_top
    margin-top: 35px;
  .input_search
    display: flex;
    justify-content: space-between;
    align-items: center;
  .marginvi
    margin-left: 0;
  .search
    font-size: 14px;
    margin-left: 10px;
    .labeltext
      margin-right: 10px
    .line
      padding: 0 5px;
      color: #333
    .el-date-editor.el-input, .el-date-editor.el-input__inner
      width: 145px;
    .el-input
      width: 170px;
  .select
    margin-left: 20px;
    .label
      margin-right: 10px;
    .el-select, .el-select--medium
      width: 170px;
</style>
