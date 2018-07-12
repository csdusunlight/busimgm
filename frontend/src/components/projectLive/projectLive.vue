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
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.results" style="width: 100%">
          <el-table-column label="项目编号" prop="id"></el-table-column>
          <el-table-column label="项目名称" prop="name"></el-table-column>
          <el-table-column label="立项日期" prop="name"></el-table-column>
          <el-table-column label="结项日期" prop="name"></el-table-column>
          <el-table-column label="预计待收/待消耗" prop="name"></el-table-column>
          <el-table-column label="预计总消耗" prop="name"></el-table-column>
          <el-table-column label="总返现金额" prop="name"></el-table-column>
          <el-table-column label="预估渠道消耗" prop="name"></el-table-column>
          <el-table-column label="渠道返现金额" prop="name"></el-table-column>
          <el-table-column label="预估网站消耗" prop="name"></el-table-column>
          <el-table-column label="网站返现金额" prop="name"></el-table-column>
          <el-table-column label="项目状态" prop="name"></el-table-column>
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
import {getProjectLive} from '@/api/api'
export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      projectnum: '',
      projectname: '',
      selectvalue: '0',
      loading: true,
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
