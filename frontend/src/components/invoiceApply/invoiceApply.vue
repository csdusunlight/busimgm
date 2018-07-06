<template>
  <div class="invoiceadmin">
    <el-row>
      <el-col :span="24">
        <div class="input_search">
          <div class="search marginvi search_box">
            <label class="labeltext">日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate0" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate1" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
          <div class="search search_box">
            <label class="labeltext">开票日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate2" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate3" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
          <div class="search">
            <label class="labeltext">项目名称</label>
            <el-input size="medium" v-model="projectname"></el-input>
          </div>
          <div class="search">
            <label class="labeltext">发票类型</label>
            <el-select size="medium" v-model="invoicetype" placeholder="请选择">
              <el-option
                v-for="item in invoicetypeop"
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
        <div class="select">
          <label class="label">审核状态</label>
          <el-select size="medium" v-model="examinestate" placeholder="请选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="flexright">
          <el-button size="medium" type="primary" @click="searchBtn">搜索</el-button>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="4" :offset="20">
        <div class="flexright">
          <el-button size="medium" type="info" @click="invoiceApply">发票申请</el-button>
        </div>
      </el-col>
      <el-dialog
        title="发票申请"
        :visible.sync="dialogVisible"
        width="50%"
        >
        <div class="form_table">
          <el-form :model="invoice" :rules="rules" ref="invoice" label-width="120px" class="demo-ruleForm">
            <el-form-item label="项目名称" prop="project">
              <el-select size="medium" v-model="invoice.project" placeholder="请选择">
                <el-option
                  v-for="item in projectOption"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="发票类型" prop="invoice_type">
              <el-radio-group v-model="invoice.invoice_type">
                <el-radio :label="0">专票</el-radio>
                <el-radio :label="1">普票</el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="开票日期" prop="invoice_date">
              <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="invoice.invoice_date" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            </el-form-item>
            <el-form-item label="签约公司" prop="contract_company">
              <el-input v-model="invoice.contract_company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="company">
              <el-input v-model="invoice.company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="纳税人识别号" prop="putaxmanid">
              <el-input v-model="invoice.putaxmanid" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="注册地址" prop="regaddress">
              <el-input v-model="invoice.regaddress" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="银行账号" prop="bank_account">
              <el-input v-model="invoice.bank_account" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开户行" prop="bank">
              <el-input v-model="invoice.bank" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="电话" prop="mobile">
              <el-input v-model="invoice.mobile" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开票金额" prop="invoice_num">
              <el-input v-model="invoice.invoice_num" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="record">
              <el-input type="textarea" v-model="invoice.record" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="subInvoiceForm('invoice')">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.results" style="width: 100%">
          <el-table-column label="日期" prop="apply_date" width="100"></el-table-column>
          <el-table-column label="项目名称" prop="projectname"></el-table-column>
          <el-table-column label="开票日期" prop="invoice_date"></el-table-column>
          <el-table-column label="发票类型">
            <template slot-scope="scope">
              <span>{{invoiceFilter[scope.row.invoice_type]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="签约公司" prop="contract_company" width="100"></el-table-column>
          <el-table-column label="甲方公司名称" prop="company"></el-table-column>
          <el-table-column label="开票金额" prop="invoice_num"></el-table-column>
          <el-table-column label="审核状态" prop="invoice_state">
            <template slot-scope="scope">
              <span>{{stateFilter[scope.row.state]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="备注" prop="record"></el-table-column>
          <el-table-column label="操作" v-if="operationShow">
            <template slot-scope="scope">
              <div class="operation_button">
                <div class="op_button_padding"><el-button size="mini" type="danger" @click="opInvoice(scope.row)">修改</el-button></div>
                <div class="op_button_padding"><el-button size="mini" type="warning" @click="deleteInvoiceBtn(scope.row)">删除</el-button></div>
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
        title="发票修改"
        :visible.sync="invoiceVisible"
        width="50%"
        >
        <div class="form_table">
          <el-form :model="modifyInvoice" :rules="modifyInvoice" ref="modifyInvoice" label-width="120px" class="demo-ruleForm">
            <el-form-item label="项目名称" prop="project">
              <el-select size="medium" filterable v-model="invoice.project" placeholder="请选择">
                <el-option
                  v-for="item in projectOption"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="发票类型" prop="invoice_type">
              <el-radio v-model="modifyInvoice.invoice_type" label="0">专票</el-radio>
              <el-radio v-model="modifyInvoice.invoice_type" label="1">普票</el-radio>
            </el-form-item>
            <el-form-item label="开票日期" prop="invoice_date">
              <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="modifyInvoice.invoice_date" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            </el-form-item>
            <el-form-item label="签约公司" prop="contract_company">
              <el-input v-model="modifyInvoice.contract_company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="company">
              <el-input v-model="modifyInvoice.company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="纳税人识别号" prop="putaxmanid">
              <el-input v-model="modifyInvoice.putaxmanid" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="注册地址" prop="regaddress">
              <el-input v-model="modifyInvoice.regaddress" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="银行账号" prop="bank_account">
              <el-input v-model="modifyInvoice.bank_account" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开户行" prop="bank">
              <el-input v-model="modifyInvoice.bank" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="电话" prop="mobile">
              <el-input v-model="modifyInvoice.mobile" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开票金额" prop="invoice_num">
              <el-input v-model="modifyInvoice.invoice_num" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="record">
              <el-input type="textarea" v-model="modifyInvoice.record" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="invoiceVisible = false">取 消</el-button>
          <el-button type="primary" @click="subModifyInvoice">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
  </div>
</template>

<script>
import {examineOption, examineFilter} from '@/common/js/options'
import {postInvoice, getInvoice, putInvoice, deleteInvoice, allGetProject} from '@/api/api'

export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      inputdate2: '',
      inputdate3: '',
      projectname: '',
      invoicetype: '',
      examinestate: '0',
      options: examineOption,
      dialogVisible: false,
      invoiceVisible: false,
      loading: true,
      operationShow: true,
      currentPage: 1,
      dataList: [],
      stateFilter: examineFilter,
      invoicetypeop: [
        {
          value: '',
          label: '全部'
        },
        {
          value: '0',
          label: '专票'
        },
        {
          value: '1',
          label: '普票'
        }
      ],
      invoiceFilter: {0: '专票', 1: '普票'},
      putId: '',
      projectOption: [],
      invoice: {
        project: '',
        invoice_type: '',
        invoice_date: '',
        contract_company: '',
        company: '',
        putaxmanid: '',
        regaddress: '',
        bank_account: '',
        bank: '',
        mobile: '',
        invoice_num: '',
        record: ''
      },
      rules: {
        project: [
          { required: true, message: '选择项目', trigger: 'blur' }
        ],
        invoice_type: [
          { required: true, message: '选择发票类型', trigger: 'blur' }
        ],
        invoice_date: [
          { required: true, message: '选择开票时间', trigger: 'blur' }
        ],
        contract_company: [
          { required: true, message: '请输入签约公司', trigger: 'blur' }
        ],
        company: [
          { required: true, message: '请输入甲方公司公司', trigger: 'blur' }
        ],
        putaxmanid: [
          { required: true, message: '请输入纳税人识别号', trigger: 'blur' }
        ],
        regaddress: [
          { required: true, message: '请输入注册地址', trigger: 'blur' }
        ],
        bank_account: [
          { required: true, message: '请输入银行账号', trigger: 'blur' }
        ],
        bank: [
          { required: true, message: '请输入开户行', trigger: 'blur' }
        ],
        mobile: [
          { required: true, message: '请输入电话', trigger: 'blur' }
        ],
        invoice_num: [
          { required: true, message: '请输入金额', trigger: 'blur' }
        ]
      },
      modifyInvoice: {
        id: '',
        invoice_type: ''
      }
    }
  },
  created () {
    this.getDatalist()
  },
  methods: {
    invoiceApply () {
      this.dialogVisible = true
    },
    /* 获取列表 */
    getDatalist () {
      let data = this.conditionDate()
      if (this.examinestate === '0') {
        this.operationShow = true
      } else {
        this.operationShow = false
      }
      getInvoice(this.currentPage, data).then((res) => {
        console.log(res)
        this.dataList = res.data
        this.loading = false
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
          invoice_date_0: this.inputdate2,
          invoice_date_1: this.inputdate3,
          projectname: this.projectname,
          invoice_type: this.invoicetype,
          state: this.examinestate
        }
      }
      return Data
    },
    /* 分页 */
    handleCurrentChange (val) {
      this.datalist = []
      this.loading = true
      this.currentPage = val
      this.getDatalist()
    },
    /* 新建发票提交 */
    subInvoiceForm (invoice) {
      this.$refs[invoice].validate((valid) => {
        if (valid) {
          postInvoice(this.invoice).then((res) => {
            if (res.data.code === 0) {
              /* this.invoice = this.initInvoice */
              this.$refs[invoice].resetFields()
              this.$message({
                type: 'success',
                message: '发票申请成功!'
              })
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
    /* 发票修改 */
    subModifyInvoice () {
      putInvoice(this.modifyInvoice.id, this.modifyInvoice).then((res) => {
        console.log(res)
        this.$message({
          type: 'success',
          message: '修改成功!'
        })
        this.invoiceVisible = false
        this.loading = true
        this.getDatalist()
      }).catch((err) => {
        this.invoiceVisible = false
        console.log(err)
      })
    },
    /* 打开发票修改对话框 */
    opInvoice (row) {
      this.invoiceVisible = true
      Object.assign(this.modifyInvoice, row)
      console.log(this.modifyInvoice)
    },
    /* 发票删除 */
    deleteInvoiceBtn (row) {
      this.$confirm('此操作将永久删除该发票, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteInvoice(row.id).then((res) => {
          if (res.data.code === '0') {
            this.$message({
              type: 'success',
              message: '删除成功!'
            })
            this.loading = true
            this.getDatalist()
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
    /* 搜索 */
    searchBtn () {
      this.loading = true
      this.currentPage = 1
      this.getDatalist()
    }
  },
  mounted () {
    this.getProjectList()
  },
  watch: {
    examinestate () {
      this.dataList = []
      this.loading = true
      this.currentPage = 1
      this.getDatalist()
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.invoiceadmin
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
      padding-left: 15px
    .el-input--suffix .el-input__inner
      padding-right: 15px
    .el-input__suffix
      right: 0;
    .el-input
      width: 140px;
  .flexright
    display: flex;
    justify-content: flex-end;
  .select
    .label
      margin-right: 12px;
</style>
