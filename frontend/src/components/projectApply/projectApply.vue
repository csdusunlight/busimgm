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
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="24">
        <div class="flexright">
          <el-button size="medium" @click="newAddproject()" type="info">新增项目</el-button>
        </div>
      </el-col>
      <el-dialog
        title="项目申请"
        :visible.sync="dialogVisible"
        width="50%"
        >
        <div class="form_table">
          <el-form :model="addProject" :rules="rules" ref="addProject" label-width="120px" class="demo-ruleForm">
            <el-form-item label="项目名称" prop="resource">
              <el-input v-model="addProject.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="resource">
              <el-input v-model="addProject.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="平台名称" prop="resource">
              <el-input v-model="addProject.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="对公对私">
              <el-input v-model="addProject.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="结算方式" prop="resource">
              <el-input v-model="addProject.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="签约公司" prop="resource">
              <el-input v-model="addProject.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="合作详情" prop="resource">
              <el-input v-model="addProject.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="resource">
              <el-input type="textarea" v-model="addProject.resource" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
        </span>
      </el-dialog>
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
      dialogVisible: false,
      addProject: {
        resource: ''
      },
      rules: {
        resource: [
          { required: true, message: '项目名称', trigger: 'blur' }
        ]
      },
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
          label: '待审核'
        },
        {
          value: '1',
          label: '审核拒绝'
        },
        {
          value: '2',
          label: '进行中'
        },
        {
          value: '3',
          label: '结项中'
        },
        {
          value: '4',
          label: '已结项'
        },
        {
          value: '5',
          label: '结项失败'
        }
      ]
    }
  },
  methods: {
    newAddproject () {
      this.dialogVisible = true
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
