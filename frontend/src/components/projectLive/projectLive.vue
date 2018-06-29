<template>
  <div class="projectLive">
    <el-row >
      <el-col :span="22">
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
        </div>
      </el-col>
      <el-col :span="2">
        <div class="flexright">
          <el-button size="medium" type="primary">搜索</el-button>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="8">
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
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="4" :offset="20">
        <div class="flexright">
          <el-button size="medium" type="info">导出</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      projectnum: '',
      projectname: '',
      selectvalue: '0',
      options: [
        {
          value: '0',
          label: '全部'
        },
        {
          value: '1',
          label: '正在进行'
        },
        {
          value: '2',
          label: '已结项'
        }
      ]
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
      margin-right: 12px;
  .row_top
    margin-top: 35px;
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
</style>
