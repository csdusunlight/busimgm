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
          <el-button size="medium" type="primary" @click="searchBtn">搜索</el-button>
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
        title="费用申请"
        :visible.sync="dialogVisible"
        width="50%"
        >
        <div class="form_table">
          <el-form :model="addCostApply" :rules="rules" ref="addCostApply" label-width="120px" class="demo-addCostApply">
            <el-form-item label="项目名称" prop="project">
              <el-select size="medium" v-model="addCostApply.project" placeholder="请选择">
                <el-option
                  label="小明有限公司"
                  value="小明有限公司">
                </el-option>
                <el-option
                  label="小方有限公司"
                  value="小方有限公司">
                </el-option>
                <el-option
                  label="小云有限公司"
                  value="小云有限公司">
                </el-option>
                <el-option
                  label="小园有限公司"
                  value="小园有限公司">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="打款截图" prop="send_pic">
              <div class="img_long">
                <el-upload
                  class="avatar-uploader"
                  action="http://upload-z2.qiniup.com"
                  :data="imgData"
                  :show-file-list="false"
                  :on-success="handleAvatarSuccess"
                  :before-upload="beforeAvatarUpload"
                  >
                  <img v-if="addCostApply.send_pic" ref="extensionimg" :src="addCostApply.send_pic" class="avatar">
                  <i v-else :class="[uploadIcon ? 'el-icon-loading' : 'el-icon-plus']" class="avatar-uploader-icon"></i>
                </el-upload>
                <span @click="unsend_pic">删除长图 </span>
              </div>
            </el-form-item>
            <el-form-item label="对公对私" prop="fundtype">
              <el-select size="medium" v-model="addCostApply.fundtype" placeholder="请选择">
                <el-option
                  v-for="item in paccountypeops"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="打款时间" prop="send_date">
              <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="addCostApply.send_date" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            </el-form-item>
            <el-form-item label="打款金额" prop="fund_rec">
              <el-input v-model="addCostApply.fund_rec" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="company">
              <el-input v-model="addCostApply.company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="record">
              <el-input type="textarea" v-model="addCostApply.record" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="postCostData('addCostApply')">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
    <el-row class="row_top row_buttom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.results" style="width: 100%">
          <el-table-column label="日期" prop="apply_date"></el-table-column>
          <el-table-column label="项目名称" prop="project"></el-table-column>
          <el-table-column label="打款金额" prop="fund_rec"></el-table-column>
          <el-table-column label="打款时间" prop="send_date"></el-table-column>
          <el-table-column label="打款截图">
            <template slot-scope="scope">
              <div class="img_box">
                <img :src="scopr.row.send_pic"/>
              </div>
            </template>
          </el-table-column>
          <el-table-column label="对公对私">
            <template slot-scope="scope">
              <span>{{paccountFliter[scope.row.fundtype]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="甲方公司名称" prop="company"></el-table-column>
          <el-table-column label="审核状态" prop="invoicenum">
            <template slot-scope="scope">
              <span>{{examineFilters[scope.row.audit_state]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="备注" prop="record"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <div class="operation_button">
                <div class="op_button_padding"><el-button size="mini" type="danger" @click="modifyCost(scope.row)">修改</el-button></div>
                <div class="op_button_padding"><el-button size="mini" type="warning" @click="deleteCost(scope.row)">删除</el-button></div>
              </div>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </el-row>
  </div>
</template>

<script>
import {examineOption, paccounOption, paccountypeopsFilter, examineFilter} from '@/common/js/options'
import {getToken, getCostList, postCost} from '@/api/api'

export default {
  data () {
    return {
      projectnum: '',
      projectname: '',
      onwcopte: '',
      selectvalue: '0',
      options: examineOption,
      dataList: [],
      dialogVisible: false,
      uploadIcon: false,
      loading: true,
      paccountypeops: paccounOption,
      paccountFliter: paccountypeopsFilter,
      examineFilters: examineFilter,
      currentPage: 1,
      searchState: 0,
      addCostApply: {
        project: '',
        send_pic: '',
        fundtype: '',
        fund_rec: '',
        company: '',
        send_date: ''
      },
      initAddCostApply: {
        project: '',
        send_pic: '',
        fundtype: '',
        fund_rec: '',
        company: '',
        send_date: ''
      },
      rules: {
        project: [
          { required: true, message: '项目名称', trigger: 'blur' }
        ],
        send_pic: [
          { required: true, message: '请上传打款截图', trigger: 'blur' }
        ],
        fundtype: [
          { required: true, message: '请选择公私类型', trigger: 'blur' }
        ],
        fund_rec: [
          { required: true, message: '请选择打款金额', trigger: 'blur' }
        ],
        company: [
          { required: true, message: '请输入甲方公司名称', trigger: 'blur' }
        ],
        send_date: [
          { required: true, message: '请选择打款时间', trigger: 'blur' }
        ]
      },
      imgData: {
        token: '',
        key: ''
      }
    }
  },
  created () {
    this.getCostDatalist()
  },
  methods: {
    /* 费用申请列表 */
    getCostDatalist () {
      let data = this.conditionDate()
      getCostList(this.currentPage, data).then((res) => {
        console.log(res)
        this.loading = false
      }).catch((err) => {
        console.log(err)
      })
    },
    /* 打开费用申请表 */
    costApplyBtn () {
      this.dialogVisible = true
    },
    /* 图片上传完成后 */
    handleAvatarSuccess (res, file) {
      console.log(res)
      console.log(file)
      this.addCostApply.send_pic = `http://image.fuliunion.com/${res.key}`
    },
    /* 图片上传前获取token值 */
    beforeAvatarUpload (file) {
      this.addCostApply.send_pic = ''
      this.uploadIcon = true
      return getToken().then((res) => {
        this.imgData.token = res.data.token
        this.imgData.key = res.data.key
      })
    },
    /* 删除图片 */
    unsend_pic () {
      this.addCostApply.send_pic = ''
      this.uploadIcon = false
    },
    /* 确定提交费用申请 */
    postCostData (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          postCost(this.addCostApply).then((res) => {
            if (res.data.code === 0) {
              this.addCostApply = this.initAddCostApply
              this.$refs[formName].resetFields()
              this.$message({
                type: 'success',
                message: '新建费用申请成功!'
              })
              this.dialogVisible = false
              this.getCostDatalist()
            } else {
              this.dialogVisible = false
              this.$message(res.data.detail)
            }
          }).catch((err) => {
            console.log(err)
          })
        } else {
          this.$message.error('提交有误，请检查提交项！')
          return false
        }
      })
    },
    /* 修改费用申请 */
    modifyCost (row) {
    },
    /* 删除费用申请 */
    deleteCost (row) {
    },
    /* 搜索 */
    searchBtn () {
      this.searchState = 2
      this.currentPage = 1
      this.getCostDatalist()
    },
    /* 搜索条件拼接 */
    conditionDate () {
      let Data = {}
      if (this.searchState === 0) {
        Data = {
          params: {
            audit_state: this.selectvalue
          }
        }
      } else {
        Data = {
          params: {
            id: this.projectnum,
            project: this.projectname,
            company: this.onwcopte,
            audit_state: this.selectvalue
          }
        }
      }
      return Data
    }
  },
  watch: {
    selectvalue () {
      this.searchState = 0
      this.currentPage = 1
      this.getCostDatalist()
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
