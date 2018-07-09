<template>
  <div class="costadmin">
    <el-row >
      <el-col :span="24">
        <div class="input_search">
          <div class="search marginvi search_box">
            <label class="labeltext">申请日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate0" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate1" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
          <div class="search">
            <label class="labeltext">项目名称</label>
            <el-input size="medium" v-model="projectname"></el-input>
          </div>
          <div class="search">
            <label class="labeltext">甲方公司</label>
            <el-input size="medium" v-model="onwcopte"></el-input>
          </div>
          <div class="select">
            <label class="label">对公对私</label>
            <el-select size="medium" v-model="fundtypevalue" placeholder="请选择">
              <el-option
                v-for="item in fundtypeOption"
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
      <el-col :span="20">
        <div class="flex_default">
          <div class="search marginvi search_box">
            <label class="labeltext">打款日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate2" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate3" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
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
        </div>
      </el-col>
      <el-col :span="4">
        <div class="flexright">
          <el-button size="medium" type="primary" @click="searchBtn">搜索</el-button>
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
              <el-select size="medium" filterable v-model="addCostApply.project" placeholder="请选择">
                <el-option
                  v-for="item in projectOption"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
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
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.results" style="width: 100%">
          <el-table-column label="日期" prop="apply_date"></el-table-column>
          <el-table-column label="项目名称" prop="projectname"></el-table-column>
          <el-table-column label="打款金额" prop="fund_rec"></el-table-column>
          <el-table-column label="打款时间" prop="send_date"></el-table-column>
          <el-table-column label="打款截图">
            <template slot-scope="scope">
              <div class="img_box">
                <img :src="scope.row.send_pic"/>
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
              <span>{{examineFilters[scope.row.state]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="备注" prop="record"></el-table-column>
          <el-table-column label="操作" v-if="operationShow">
            <template slot-scope="scope">
              <div class="operation_button">
                <div class="op_button_padding"><el-button size="mini" type="danger" @click="modifyCostBtn(scope.row)">修改</el-button></div>
                <div class="op_button_padding"><el-button size="mini" type="warning" @click="deleteCostBtn(scope.row)">删除</el-button></div>
              </div>
            </template>
          </el-table-column>
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
      <el-dialog
        title="费用修改"
        :visible.sync="modifyVisible"
        width="50%"
        >
        <div class="form_table">
          <el-form :model="modifyCost" :rules="rules" ref="modifyCost" label-width="120px" class="demo-modifyCost">
            <el-form-item label="项目名称" prop="project" >
              <el-select size="medium" filterable v-model="modifyCost.project" placeholder="请选择">
                <el-option
                  v-for="item in projectOption"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
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
                  :on-success="modifyAvatarSuccess"
                  :before-upload="modifyAvatarUpload"
                  >
                  <img v-if="modifyCost.send_pic" ref="extensionimg" :src="modifyCost.send_pic" class="avatar">
                  <i v-else :class="[modifyuploadIcon ? 'el-icon-loading' : 'el-icon-plus']" class="avatar-uploader-icon"></i>
                </el-upload>
                <span @click="modifyUnSend_pic">删除长图 </span>
              </div>
            </el-form-item>
            <el-form-item label="对公对私" prop="fundtype">
              <el-select size="medium" v-model="modifyCost.fundtype" placeholder="请选择">
                <el-option
                  v-for="item in paccountypeops"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="打款时间" prop="send_date">
              <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="modifyCost.send_date" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            </el-form-item>
            <el-form-item label="打款金额" prop="fund_rec">
              <el-input v-model="modifyCost.fund_rec" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="company">
              <el-input v-model="modifyCost.company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="record">
              <el-input type="textarea" v-model="modifyCost.record" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="modifyCostData('modifyCost')">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
  </div>
</template>

<script>
import {examineOption, paccounOption, paccountypeopsFilter, examineFilter} from '@/common/js/options'
import {getToken, getCostList, postCost, allGetProject, deleteCost, putCost} from '@/api/api'

export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      inputdate2: '',
      inputdate3: '',
      projectnum: '',
      projectname: '',
      onwcopte: '',
      selectvalue: '0',
      fundtypevalue: '',
      options: examineOption,
      dataList: [],
      dialogVisible: false,
      modifyVisible: false,
      uploadIcon: false,
      modifyuploadIcon: false,
      loading: true,
      operationShow: true,
      fundtypeOption: [
        {
          value: '',
          label: '全部'
        },
        {
          value: '1',
          label: '对私'
        },
        {
          value: '0',
          label: '对公'
        }
      ],
      paccountypeops: paccounOption,
      paccountFliter: paccountypeopsFilter,
      examineFilters: examineFilter,
      currentPage: 1,
      searchState: 0,
      projectOption: [],
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
      modifyCost: {
        project: '',
        send_pic: '',
        fundtype: '',
        fund_rec: '',
        company: '',
        send_date: ''
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
      if (this.selectvalue === '0') {
        this.operationShow = true
      } else {
        this.operationShow = false
      }
      getCostList(this.currentPage, data).then((res) => {
        console.log(res)
        this.loading = false
        this.dataList = res.data
        console.log(this.dataList)
      }).catch((err) => {
        console.log(err)
      })
    },
    /* 搜索条件拼接 */
    conditionDate () {
      let Data = {
        params: {
          apply_date_0: this.inputdate0,
          apply_date_1: this.inputdate1,
          send_date_0: this.inputdate2,
          send_date_1: this.inputdate3,
          projectname: this.projectname,
          company: this.onwcopte,
          state: this.selectvalue,
          fundtype: this.fundtypevalue
        }
      }
      return Data
    },
    /* 打开费用申请表 */
    costApplyBtn () {
      this.dialogVisible = true
    },
    /* 图片上传完成后 */
    handleAvatarSuccess (res, file) {
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
    /* moidfy图片上传后 */
    modifyAvatarSuccess (res, file) {
      this.modifyCost.send_pic = `http://image.fuliunion.com/${res.key}`
    },
    /* modify图片上传前获取token值 */
    modifyAvatarUpload (file) {
      this.modifyCost.send_pic = ''
      this.modifyuploadIcon = true
      return getToken().then((res) => {
        this.imgData.token = res.data.token
        this.imgData.key = res.data.key
      })
    },
    /* modify删除图片 */
    modifyUnSend_pic () {
      this.addCostApply.send_pic = ''
      this.modifyCost.send_pic = ''
      this.modifyuploadIcon = false
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
              this.loading = true
              this.dialogVisible = false
              this.getCostDatalist()
              this.uploadIcon = false
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
    /* 获取项目 */
    getProjectList () {
      allGetProject().then((res) => {
        console.log(res.data)
        res.data.results.forEach((val, i) => {
          this.projectOption.push({
            'value': val.id.toString(),
            'label': val.name
          })
        })
        console.log(this.projectOption)
      }).catch((err) => {
        console.log(err)
      })
    },
    /* 分页 */
    handleCurrentChange (val) {
      this.loading = true
      this.currentPage = val
      this.getCostDatalist()
    },
    /* 修改费用申请 */
    modifyCostBtn (row) {
      this.modifyVisible = true
      Object.assign(this.modifyCost, row)
    },
    /* 提交修改费用 */
    modifyCostData () {
      putCost(this.modifyCost.id, this.modifyCost).then((res) => {
        console.log(res)
        this.$message({
          type: 'success',
          message: '修改成功!'
        })
        this.loading = true
        this.modifyVisible = false
        this.getCostDatalist()
      }).catch((err) => {
        this.modifyVisible = false
        console.log(err)
      })
    },
    /* 删除费用申请 */
    deleteCostBtn (row) {
      this.$confirm('此操作将永久删除该申请, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteCost(row.id).then((res) => {
          if (res.data.code === '0') {
            console.log(res)
            this.$message({
              type: 'success',
              message: '删除成功!'
            })
            this.loading = true
            this.getCostDatalist()
          } else {
            this.$message(res.data.detail)
          }
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    /* 搜索 */
    searchBtn () {
      this.currentPage = 1
      this.getCostDatalist()
    }
  },
  mounted () {
    this.getProjectList()
  },
  watch: {
    /* 审核状态 */
    selectvalue () {
      this.dataList = []
      this.loading = true
      this.currentPage = 1
      this.getCostDatalist()
    },
    /* 对公对私 */
    fundtypevalue () {
      this.dataList = []
      this.loading = true
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
    justify-content: space-between;
    align-items: center;
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
  .marginvi
    margin-left: 0;
  .flexright
    display: flex;
    justify-content: flex-end;
  .select
    margin-left: 20px;
    .label
      margin-right: 10px;
    .el-select, .el-select--medium
      width: 170px;
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
  .img_box
    img
      width: 100px
      height: 120px
</style>
