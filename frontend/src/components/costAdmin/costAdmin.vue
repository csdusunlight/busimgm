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
          <el-button size="medium" type="info" @click="costApplyBtn">费用申请</el-button>
        </div>
      </el-col>
      <el-dialog
        title="项目申请"
        :visible.sync="dialogVisible"
        width="50%"
        >
        <div class="form_table">
          <el-form :model="addCostApply" :rules="rules" ref="addCostApply" label-width="120px" class="demo-addCostApply">
            <el-form-item label="项目名称" prop="name">
              <el-select size="medium" v-model="addCostApply.resource" placeholder="请选择">
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="打款截图" prop="costPic">
              <div class="img_long">
                <el-upload
                  class="avatar-uploader"
                  action="http://upload-z2.qiniup.com"
                  :data="imgData"
                  :show-file-list="false"
                  :on-success="handleAvatarSuccess"
                  :before-upload="beforeAvatarUpload"
                  >
                  <img v-if="addCostApply.costPic" ref="extensionimg" :src="addCostApply.costPic" class="avatar">
                  <i v-else :class="[uploadIcon ? 'el-icon-loading' : 'el-icon-plus']" class="avatar-uploader-icon"></i>
                </el-upload>
                <span @click="unCostPic">删除长图 </span>
              </div>
            </el-form-item>
            <el-form-item label="对公对私" prop="platname">
              <el-input v-model="addCostApply.platname" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="打款时间">
              <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="addCostApply.platname" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            </el-form-item>
            <el-form-item label="打款金额" prop="resource">
              <el-input v-model="addCostApply.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="resource">
              <el-input v-model="addCostApply.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="resource">
              <el-input type="textarea" v-model="addCostApply.resource" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="postCostData">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
  </div>
</template>

<script>
import {examineOption} from '@/common/js/options'
import {getToken} from '@/api/api'
export default {
  data () {
    return {
      projectnum: '',
      projectname: '',
      onwcopte: '',
      selectvalue: '0',
      options: examineOption,
      dialogVisible: false,
      uploadIcon: false,
      addCostApply: {
        resource: '',
        costPic: ''
      },
      rules: {
        resource: [
          { required: true, message: '项目名称', trigger: 'blur' }
        ],
        costPic: [
          { required: true, message: '上传截图', trigger: 'blur' }
        ]
      },
      imgData: {
        token: '',
        key: ''
      }
    }
  },
  methods: {
    /* 打开费用申请表 */
    costApplyBtn () {
      this.dialogVisible = true
    },
    /* 图片上传完成后 */
    handleAvatarSuccess (res, file) {
      console.log(res)
      console.log(file)
      this.addCostApply.costPic = `http://img.fuliunion.com/${res.key}`
    },
    /* 图片上传前获取token值 */
    beforeAvatarUpload (file) {
      this.addCostApply.costPic = ''
      this.uploadIcon = true
      return getToken().then((res) => {
        this.imgData.token = res.data.token
        this.imgData.key = res.data.key
      })
    },
    /* 删除图片 */
    unCostPic () {
      this.addCostApply.costPic = ''
      this.uploadIcon = false
    },
    /* 确定提交费用申请 */
    postCostData () {
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
  .img_long
    margin-top:10px;
    display:flex;
    align-items: flex-end;
    span
      font-size: 12px;
      padding-left: 10px;
      cursor: pointer;
      color: #6d81fc
    .avatar-uploader .el-upload
      border: 1px dashed #d9d9d9;
      border-radius: 6px;
      cursor: pointer;
      position: relative;
      overflow: hidden;
    .avatar-uploader .el-upload:hover
      border-color: #409EFF;
    .avatar-uploader-icon
      font-size: 28px;
      color: #8c939d;
      width: 90px;
      height: 90px;
      line-height: 90px;
      text-align: center;
    .avatar
      width: 90px;
      height: 90px;
      display: block;
</style>
