<template>
  <div class="costadmin">
    <el-row >
      <el-col :span="22">
        <div class="input_search">
          <div class="search">
            <label class="labeltext">项目编号</label>
            <el-input size="medium" v-model="projectnum"></el-input>
          </div>
          <div class="search">
            <label class="labeltext">项目名称</label>
            <el-input size="medium" v-model="projectname"></el-input>
          </div>
          <div class="search">
            <label class="labeltext">甲方公司</label>
            <el-input size="medium" v-model="onwcopte"></el-input>
          </div>
        </div>
      </el-col>
      <el-col :span="2">
        <div class="flexright">
          <el-button size="medium" type="primary">搜索</el-button>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="24">
        <div class="select">
          <label class="label">审核状态</label>
          <el-select size="medium" v-model="selectvalue" placeholder="请选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="24">
        <div class="flexright">
          <el-button size="medium" type="info">费用申请</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import {examineOption} from '@/common/js/options'

export default {
  data () {
    return {
      projectnum: '',
      projectname: '',
      onwcopte: '',
      selectvalue: '0',
      options: examineOption
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.costadmin
  .input_search
    display: flex;
    align-items: center;
  .search
    margin-right: 20px;
    font-size: 14px;
    .labeltext
      padding-right: 12px
    .line
      padding: 0 5px;
      color: #333
    .el-date-editor.el-input, .el-date-editor.el-input__inner
      width: 140px;
    .el-input
      width: 170px;
  .flexright
    display: flex;
    justify-content: flex-end;
    padding-right: 18px;
  .select
    .label
      margin-right: 12px;
</style>
