<template>
  <div class="dataadmin">
    <el-row>
      <el-col :span="24">
        <div class="input_search">
          <div class="search marginvi search_box">
            <label class="labeltext">投资日期</label>
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
            <el-input size="medium" v-model="projectnameVal"></el-input>
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
          <div class="select margin_clear">
            <label class="label">投资来源</label>
            <el-select size="medium" v-model="investvalue" placeholder="请选择">
              <el-option
                v-for="item in investment"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
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
      </el-col>
      <el-col :span="4">
        <div class="flexright">
          <el-button size="medium" type="primary" @click="searchBtn">搜索</el-button>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <div class="flexright">
          <el-upload
            class="avatar-uploader"
            :action="uploadURL1"
            :name="uploadName"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload">
            <el-button size="medium" type="info">导入</el-button>
          </el-upload>
          <el-button @click="exportExel" size="medium" type="info">导出</el-button>
          <el-upload
            class="avatar-uploader"
            :action="uploadURL3"
            :name="uploadName"
            :with-credentials= "true"
            :show-file-list="false"
            :on-success="handleThreeSuccess"
            :before-upload="beforeAvatarUpload">
            <el-button size="medium" type="info">审核数据导入</el-button>
          </el-upload>
          <el-upload
            class="avatar-uploader"
            :action="uploadURL4"
            :name="uploadName"
            :with-credentials= "true"
            :show-file-list="false"
            :on-success="handleFourSuccess"
            :before-upload="beforeAvatarUpload">
            <el-button size="medium" type="info">异常数据导入</el-button>
          </el-upload>
          <a href="http://mgm.fuliunion.com/static/projectdata_init_template.xls"><el-button size="medium" type="info">获取初始导入模板</el-button></a>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.results" style="width: 100%">
          <el-table-column label="项目编号" prop="project" width="100"></el-table-column>
          <el-table-column label="项目名称" prop="projectname"></el-table-column>
          <el-table-column label="投资日期" prop="invest_time"></el-table-column>
          <el-table-column label="是否复投" prop="is_futou">
            <template slot-scope="scope">
              <span v-if="scope.row.is_futou">复投</span>
              <span v-else>首投</span>
            </template>
          </el-table-column>
          <el-table-column label="提交手机号" prop="invest_mobile" width="100"></el-table-column>
          <el-table-column label="投资金额" prop="invest_amount"></el-table-column>
          <el-table-column label="投资标期" prop="invest_term"></el-table-column>
          <el-table-column label="预估消耗" prop="settle_amount"></el-table-column>
          <el-table-column label="投资来源">
            <template slot-scope="scope">
              <span>{{sourceFilter[scope.row.source]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="返现金额" prop="return_amount"></el-table-column>
          <el-table-column label="审核状态">
            <template slot-scope="scope">
              <span>{{stateFilter[scope.row.state]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="审核时间" prop="audit_time"></el-table-column>
          <el-table-column label="备注" prop="remark"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <div class="operation_minimalism">
                <span class="minimalism"><el-button size="mini" type="danger" @click="AgreeDataAdminBtn(scope.row)">审核</el-button></span>
                |
                <span class="minimalism"><el-button size="mini" type="warning" @click="deleteDataAdminBtn(scope.row)">删除</el-button></span>
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
        title="审核数据"
        :visible.sync="dialogVisible"
        width="35%"
        >
        <div class="form_table">
          <el-form :model="examineReason" :rules="rules" ref="examineReason" label-width="120px" class="demo-ruleForm">
            <el-form-item label="投资来源" prop="source">
              <el-radio-group v-model="examineReason.source">
                <el-radio :label="'site'">网站</el-radio>
                <el-radio :label="'channel'">渠道</el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="返现金额" prop="return_amount">
              <el-input v-model="examineReason.return_amount"></el-input>
            </el-form-item>
            <el-form-item label="电话号码">
              <el-input v-model="examineReason.invest_mobile"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="subDataAdminBtn('examineReason')">确 定</el-button>
        </span>
      </el-dialog>
      <el-dialog
        title="一次数据导入结果"
        :visible.sync="uploadVisible"
        width="520px"
        >
        <div class="information">
          <p>总上传数据条数：{{dataAdminDetails.anum}}</p>
          <p>上传成功数据条数：{{dataAdminDetails.num}}</p>
          <p>表格重复数据条数：{{dataAdminDetails.dup1}}</p>
          <p>数据库重复数据条数：{{dataAdminDetails.dup2}}</p>
          <div class="text">重复手机号：{{dataAdminDetails.dupstr}}</div>
        </div>
      </el-dialog>
      <el-dialog
        title="审核数据导入结果"
        :visible.sync="uploadThreeVisible"
        width="520px"
        >
        <div class="information">
          <p>上传成功数据条数：{{dataAdminDetails.num}}</p>
        </div>
      </el-dialog>
    </el-row>
    <iframe id="myIFrame" scrolling="yes" style="display:none" frameborder=1></iframe>
  </div>
</template>

<script>
import {getDaAdList, agreeDataAdmin, deleteDataAdmin, normalExcel, examineExcel, abnormalExcel, exportExcel} from '@/api/api'
import {examineFilter} from '@/common/js/options'
export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      inputdate2: '',
      inputdate3: '',
      projectnum: '',
      projectnameVal: '',
      uploadURL1: normalExcel,
      uploadURL3: examineExcel,
      uploadURL4: abnormalExcel,
      exportExcelUrl: exportExcel,
      uploadName: 'file',
      subphone: '',
      investvalue: '',
      stateFilter: examineFilter,
      inmodevalue: '',
      examinestate: '',
      adoptId: '',
      dataAdminDetails: {},
      investFilter: {true: '是', false: '否'},
      sourceFilter: {'site': '网站', 'channel': '渠道'},
      dataList: [],
      loading: true,
      dialogVisible: false,
      uploadVisible: false,
      uploadThreeVisible: false,
      currentPage: 1,
      examineReason: {
        source: '',
        return_amount: ''
      },
      initExamineReason: {
        source: '',
        return_amount: ''
      },
      rules: {
        source: [
          { required: true, message: '请选择项目来源', trigger: 'blur' }
        ],
        return_amount: [
          { required: true, message: '请输入返现金额', trigger: 'blur' }
        ]
      },
      investment: [
        {
          value: '',
          label: '全部'
        },
        {
          value: 'site',
          label: '网站'
        },
        {
          value: 'channel',
          label: '渠道'
        }
      ],
      inmodeop: [
        {
          value: '',
          label: '全部'
        },
        {
          value: true,
          label: '复投'
        },
        {
          value: false,
          label: '首投'
        }
      ],
      examine: [
        {
          value: '',
          label: '全部'
        },
        {
          value: '1',
          label: '已审核'
        },
        {
          value: '0',
          label: '待审核'
        }
      ]
    }
  },
  created () {
    this.getDatalist()
  },
  methods: {
    getDatalist () {
      let data = this.conditionDate()
      getDaAdList(this.currentPage, data).then((res) => {
        this.dataList = res.data
        console.log(this.dataList)
        this.loading = false
      }).catch((err) => {
        console.log(err)
      })
    },
    /* 搜索条件拼接 */
    conditionDate () {
      let Data = {
        params: {
          investtime_0: this.inputdate0,
          investtime_1: this.inputdate1,
          audittime_0: this.inputdate2,
          audittime_1: this.inputdate3,
          project: this.projectnum,
          invest_mobile: this.subphone,
          projectname: this.projectnameVal,
          source: this.investvalue,
          is_futou: this.inmodevalue,
          state: this.examinestate
        }
      }
      return Data
    },
    /* 分页 */
    handleCurrentChange (val) {
      this.loading = true
      this.datalist = []
      this.currentPage = val
      this.getDatalist()
    },
    /* 导出数据 */
    exportExel () {
      console.log('数据导出')
      var exportUrl = this.exportExcelUrl
      console.log(exportUrl)
      var html = '<form action="' + exportUrl + '" method="get" target="_self" id="postData_form">'
      html += '<input name="investtime_0" type="hidden" value="' + this.inputdate0 + '"/>'
      html += '<input name="investtime_1" type="hidden" value="' + this.inputdate1 + '"/>'
      html += '<input name="audittime_0" type="hidden" value="' + this.inputdate2 + '"/>'
      html += '<input name="audittime_1" type="hidden" value="' + this.inputdate3 + '"/>'
      html += '<input name="project" type="hidden" value="' + this.projectnum + '"/>'
      html += '<input name="projectname" type="hidden" value="' + this.projectnameVal + '"/>'
      html += '<input name="invest_mobile" type="hidden" value="' + this.subphone + '"/>'
      html += '<input name="source" type="hidden" value="' + this.investvalue + '"/>'
      html += '<input name="is_futou" type="hidden" value="' + this.inmodevalue + '"/>'
      html += '<input name="state" type="hidden" value="' + this.examinestate + '"/>'
      html += '</form>'
      var iframe = document.getElementById('myIFrame')
      iframe.contentWindow.document.open()
      iframe.contentWindow.document.write(html)
      iframe.contentWindow.document.close()
      document.getElementById('myIFrame').contentWindow.document.getElementById('postData_form').submit()
    },
    /* 正常数据导入回调 */
    handleAvatarSuccess (response, file) {
      console.log(response)
      if (response.code === 0) {
        this.$message({
          type: 'success',
          message: '上传成功!'
        })
        this.uploadVisible = true
        this.dataAdminDetails = response.data
        this.getDatalist()
      } else {
        this.$message.error(response.detail)
      }
    },
    /* 审核数据导入回调 */
    handleThreeSuccess (response, file) {
      console.log(response)
      if (response.code === 0) {
        this.$message({
          type: 'success',
          message: '上传成功!'
        })
        this.$notify({
          title: '成功',
          message: '上传成功条数: ' + response.data.num,
          type: 'success'
        })
        this.getDatalist()
      } else {
        this.$message.error(response.detail)
      }
    },
    /* 异常数据导入回调 */
    handleFourSuccess (response, file) {
      console.log(response)
      if (response.code === 0) {
        this.$message({
          type: 'success',
          message: '上传成功!'
        })
        this.$notify({
          title: '成功',
          message: '上传成功条数: ' + response.data.num,
          type: 'success'
        })
        this.getDatalist()
      } else {
        this.$message.error(response.detail)
      }
    },
    /* 数据导入前 */
    beforeAvatarUpload () {
      this.$message('正在上传...')
    },
    /* 删除数据 */
    deleteDataAdminBtn (row) {
      this.$confirm('请确认是否删除该条数据？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteDataAdmin(row.id).then((res) => {
          console.log(res)
          if (res.data.code === 0) {
            this.$message({
              type: 'success',
              message: '操作成功!'
            })
            this.getDatalist()
          } else {
            this.$message({
              type: 'error',
              message: res.data.detail
            })
          }
        })
      }).catch(() => {
        console.log('cancel')
      })
    },
    /* 搜索 */
    searchBtn () {
      this.currentPage = 1
      this.getDatalist()
    },
    /* 同意操作 */
    AgreeDataAdminBtn (row) {
      this.dialogVisible = true
      this.adoptId = row.id
      this.examineReason.source = row.source
      this.examineReason.return_amount = row.return_amount
      this.examineReason.invest_mobile = row.invest_mobile
    },
    /* 提交同意条件 */
    subDataAdminBtn (examine) {
      this.$refs[examine].validate((valid) => {
        if (valid) {
          agreeDataAdmin(this.adoptId, this.examineReason).then((res) => {
            console.log(res)
            if (res.data.code === 0) {
              this.examineReason = this.initExamineReason
              this.$refs[examine].resetFields()
              this.$message({
                type: 'success',
                message: '审核数据成功'
              })
              this.loading = true
              this.dialogVisible = false
              this.getDatalist()
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
    tableSelectionChange (val) {
      console.log(val)
    }
  },
  watch: {
    /* 投资方式 */
    inmodevalue () {
      this.loading = true
      this.dataList = []
      this.currentPage = 1
      this.getDatalist()
    },
    /* 投资方式 */
    investvalue () {
      this.loading = true
      this.dataList = []
      this.currentPage = 1
      this.getDatalist()
    },
    /* 审核状态 */
    examinestate () {
      this.loading = true
      this.dataList = []
      this.currentPage = 1
      this.getDatalist()
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
      width: 125px;
      .el-input__prefix
        display: none;
    .el-input--prefix .el-input__inner
      padding-left: 15px
    .el-input--suffix .el-input__inner
      padding-right: 15px
    .el-input__suffix
      right: 0;
    .el-input
      width: 170px;
  .select
    .label
      margin-right: 10px;
    .el-select, .el-select--medium
      width: 170px;
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
    font-size: 14px;
    .el-button
      margin-left: 20px;
  .form_table
    padding-right: 60px;
  .information
    padding: 0 20px;
    font-size: 14px
    p
      line-height: 28px;
      width: 440px;
    .text
      text-wrap:normal;
      line-height: 28px;
      width: 440px;
      min-height: 150px;
  .table-list
    .el-table td, .el-table th
      padding: 8px 0;
    .el-table .cell
      line-height: 16px;
  .operation_minimalism
    .minimalism
      .el-button
        font-size: 12px;
        color: #171717;
        border: 0;
        padding: 0;
        background: none;
</style>
