<template>
  <div class="projectAdmin">
    <el-row>
      <el-col :span="24">
        <div class="input_search">
          <div class="search marginvi search_box">
            <label class="labeltext">立项日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate0" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
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
          <div class="search">
            <label class="labeltext">商务对接人</label>
            <el-input size="medium" v-model="takeover"></el-input>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="20">
        <div class="search marginvi inputmaxwidth">
          <label class="labeltext">签约公司</label>
          <el-input size="medium" v-model="signingCp"></el-input>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="flexright">
          <el-button size="medium" type="primary">搜索</el-button>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="24">
        <div class="flex_default">
          <div class="select margin_clear">
            <label class="label">结算方式</label>
            <el-select size="medium" v-model="settlement" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
          <div class="select margin_left">
            <label class="label">项目状态</label>
            <el-select size="medium" v-model="projectstate" placeholder="请选择">
              <el-option
                v-for="item in proOptions"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
          <div class="select margin_left">
            <label class="label">审核状态</label>
            <el-select size="medium" v-model="examinestate" placeholder="请选择">
              <el-option
                v-for="item in examineOptions"
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
      <el-col :span="24">
        <div class="flexright">
          <el-button size="medium" type="info">新增项目</el-button>
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
      takeover: '',
      signingCp: '',
      settlement: '0',
      projectstate: '0',
      examinestate: '0',
      options: [
        {
          value: '0',
          label: '全部'
        },
        {
          value: '1',
          label: '预付款'
        },
        {
          value: '2',
          label: '后付款'
        }
      ],
      proOptions: [
        {
          value: '0',
          label: '全部'
        },
        {
          value: '1',
          label: '预付款'
        },
        {
          value: '2',
          label: '后付款'
        }
      ],
      examineOptions: [
        {
          value: '0',
          label: '审核通过'
        },
        {
          value: '1',
          label: '未审核'
        },
        {
          value: '2',
          label: '审核失败'
        }
      ]
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.projectAdmin
  .input_search
    display: flex;
    justify-content: space-between;
    align-items: center;
  .search
    font-size: 14px;
    margin-left: 10px;
    .labeltext
      padding-right: 5px
    .line
      padding: 0 5px;
      color: #333
    .el-date-editor.el-input, .el-date-editor.el-input__inner
      width: 145px;
    .el-input
      width: 150px;
  .select
    .label
      margin-right: 10px;
    .el-select, .el-select--medium
      width: 160px;
  .inputmaxwidth
    .el-input
      width: 200px;
  .marginvi
    margin-left: 0;
  .flexright
    display: flex;
    justify-content: flex-end;
</style>
