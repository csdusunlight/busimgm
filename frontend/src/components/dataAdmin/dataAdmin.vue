<template>
  <div class="dataadmin">
    <el-row>
      <el-col :span="24">
        <div class="input_search">
          <div class="search marginvi search_box">
            <label class="labeltext">立项日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate0" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate1" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
          <div class="search search_box">
            <label class="labeltext">审核时间</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate2" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate3" size="medium" type="date" placeholder="选择日期"></el-date-picker>
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
    </el-row>
    <el-row>
      <el-col :span="20">
        <div class="input_search row_top">
          <div class="search marginvi">
            <label class="labeltext">提交手机号</label>
            <el-input size="medium" v-model="subphone"></el-input>
          </div>
          <div class="search">
            <div class="select">
              <label class="label">项目状态</label>
              <el-select size="medium" v-model="investvalue" placeholder="请选择">
                <el-option
                  v-for="item in investment"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </div>
          </div>
          <div class="search">
            <div class="select">
              <label class="label">投资方式</label>
              <el-select size="medium" v-model="inmodevalue" placeholder="请选择">
                <el-option
                  v-for="item in inmodeop"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </div>
          </div>
          <div class="search">
            <div class="select">
              <label class="label">审核状态</label>
              <el-select size="medium" v-model="examinestate" placeholder="请选择">
                <el-option
                  v-for="item in examine"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </div>
          </div>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="flexright">
          <el-button size="medium" type="primary">搜索</el-button>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <div class="flexright">
          <el-button size="medium" type="info">审核数据导入</el-button>
          <el-button size="medium" type="info">异常数据导出</el-button>
          <el-button size="medium" type="info">获取初始导入模板</el-button>
          <el-button size="medium" type="info">导入</el-button>
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
      inputdate2: '',
      inputdate3: '',
      projectnum: '',
      projectname: '',
      subphone: '',
      investvalue: '0',
      inmodevalue: '0',
      examinestate: '0',
      investment: [
        {
          value: '0',
          label: '全部'
        },
        {
          value: '1',
          label: '网站'
        },
        {
          value: '2',
          label: '渠道'
        }
      ],
      inmodeop: [
        {
          value: '0',
          label: '全部'
        },
        {
          value: '1',
          label: '首投'
        },
        {
          value: '2',
          label: '复投'
        }
      ],
      examine: [
        {
          value: '0',
          label: '全部'
        },
        {
          value: '1',
          label: '已审核'
        },
        {
          value: '2',
          label: '待审核'
        }
      ]
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.dataadmin
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
      width: 120px;
      .el-input__prefix
        display: none;
    .el-input--prefix .el-input__inner
      padding-left: 10px
    .el-input--suffix .el-input__inner
      padding-right: 15px
    .el-input__suffix
      right: 0;
    .el-input
      width: 140px;
    .select
      .label
        margin-right: 10px;
  .marginvi
    margin-left: 0;
  .search_box
    width: 350px;
  .row_top
    margin-top: 35px;
  .flexright
    margin-top: 35px;
    display: flex;
    justify-content: flex-end;
</style>
