<template>
  <div class="invoiceExamine">
    <el-row>
      <el-col :span="24">
        <div class="input_search">
          <div class="search marginvi">
            <label class="labeltext">申请日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate0" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate1" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
          <div class="search">
            <label class="labeltext">审核日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate2" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate3" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
          <div class="search">
            <label class="labeltext">开票日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate4" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate5" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="24">
        <div class="input_search">
          <div class="search marginvi">
            <label class="labeltext">项目名称</label>
            <el-input size="medium" v-model="projectname"></el-input>
          </div>
          <div class="search">
            <label class="labeltext">甲方公司名称</label>
            <el-input size="medium" v-model="onwcopte"></el-input>
          </div>
          <div class="search">
            <label class="labeltext">商务对接人</label>
            <el-input size="medium" v-model="toTakeOver"></el-input>
          </div>
          <div class="search">
            <label class="labeltext">审核人</label>
            <el-input size="medium" v-model="auditor"></el-input>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="20">
        <div class="flex_default">
          <div class="search marginvi">
            <label class="labeltext">签约公司</label>
            <el-input size="medium" v-model="contractCop"></el-input>
          </div>
          <div class="select">
            <label class="label">发票类型</label>
            <el-select size="medium" v-model="invoicetype" placeholder="请选择">
              <el-option
                v-for="item in invoicetypeop"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
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
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.results" style="width: 100%">
          <el-table-column label="日期" prop="apply_date"></el-table-column>
          <el-table-column label="项目名称" prop="projectname"></el-table-column>
          <el-table-column label="开票日期" prop="invoice_date"></el-table-column>
          <el-table-column label="发票类型">
            <template slot-scope="scope">
              <span>{{invoiceFilter[scope.row.invoice_type]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="签约公司" prop="contract_company"></el-table-column>
          <el-table-column label="甲方公司名称" prop="company"></el-table-column>
          <el-table-column label="纳税人识别号" prop="putaxmanid"></el-table-column>
          <el-table-column label="注册地址" prop="regaddress"></el-table-column>
          <el-table-column label="银行账号" prop="bank_account"></el-table-column>
          <el-table-column label="开户行" prop="bank"></el-table-column>
          <el-table-column label="电话" prop="mobile"></el-table-column>
          <el-table-column label="开票金额" prop="invoice_num"></el-table-column>
          <el-table-column label="商务对接人" prop="apply_man"></el-table-column>
          <el-table-column label="审核人" prop="audit_man" :key="Math.random()" v-if="examineData"></el-table-column>
          <el-table-column label="审核时间" prop="audit_date" :key="Math.random()" v-if="examineData"></el-table-column>
          <el-table-column label="拒绝原因" prop="audit_refused_reason" :key="Math.random()" v-if="examineAdopt"></el-table-column>
          <el-table-column label="备注" prop="record"></el-table-column>
          <el-table-column label="操作" :key="Math.random()" v-if="operationShow">
            <template slot-scope="scope">
              <div class="operation_button">
                <div class="op_button_padding"><el-button size="mini" type="danger" @click="invoiceAgree(scope.row)">同意</el-button></div>
                <div class="op_button_padding"><el-button size="mini" type="warning" @click="invoiceRefuse(scope.row)">拒绝</el-button></div>
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
        title="拒绝原因"
        :visible.sync="dialogVisible"
        width="35%"
        >
        <div class="form_table">
          <el-form :model="modifyinvoice" :rules="rules" ref="modifyinvoice" label-width="120px" class="demo-ruleForm">
            <el-form-item label="拒绝原因" prop="reason">
              <el-input type="textarea" v-model="modifyinvoice.reason" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="subRefuseRefuse('modifyinvoice')">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
  </div>
</template>

<script>
import {examineOption} from '@/common/js/options'
import {getInvoice, agreeInvoice, refuseInvoice} from '@/api/api'

export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      inputdate2: '',
      inputdate3: '',
      inputdate4: '',
      inputdate5: '',
      projectname: '',
      contractCop: '',
      onwcopte: '',
      toTakeOver: '',
      auditor: '',
      selectvalue: '0',
      invoicetype: '',
      examinestate: '0',
      examineData: true,
      examineAdopt: true,
      options: examineOption,
      operationShow: true,
      currentPage: 1,
      dataList: [],
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
      loading: true,
      dialogVisible: false,
      modifyinvoice: {
        reason: ''
      },
      initModifyinvoice: {
        reason: ''
      },
      rules: {
        reason: [
          { required: true, message: '请输入拒绝原因', trigger: 'blur' }
        ]
      }
    }
  },
  created () {
    this.getDatalist()
  },
  methods: {
    /* 获取列表 */
    getDatalist () {
      let data = this.conditionDate()
      if (this.selectvalue === '0') {
        this.operationShow = true
        this.examineData = false
      } else {
        this.operationShow = false
        this.examineData = true
      }
      if (this.selectvalue === '2') {
        this.examineAdopt = true
      } else {
        this.examineAdopt = false
      }
      getInvoice(this.currentPage, data).then((res) => {
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
          audit_date_0: this.inputdate2,
          audit_date_1: this.inputdate3,
          invoice_date_0: this.inputdate4,
          invoice_date_1: this.inputdate5,
          projectname: this.projectname,
          contract_company: this.contractCop,
          company: this.onwcopte,
          apply_man: this.toTakeOver,
          audit_man: this.auditor,
          invoice_type: this.invoicetype,
          state: this.selectvalue
        }
      }
      return Data
    },
    /* 分页 */
    handleCurrentChange (val) {
      this.dataList = []
      this.loading = true
      this.currentPage = val
      this.getDatalist()
    },
    sortChange (val) {
      console.log(val)
    },
    /* 同意操作 */
    invoiceAgree (row) {
      this.$confirm('请确认是否审核通过该条数据？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        agreeInvoice(row.id).then((res) => {
          if (res.data.code === 0) {
            this.$message({
              type: 'success',
              message: '操作成功!'
            })
            this.getDatalist()
          } else {
            this.$message({
              type: 'error',
              message: res.detail
            })
          }
        })
      }).catch(() => {
        console.log('cancel')
      })
    },
    /* 拒绝操作 */
    invoiceRefuse (row) {
      this.refuseId = row.id
      this.dialogVisible = true
    },
    /* 确定拒绝操作 */
    subRefuseRefuse (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          refuseInvoice(this.refuseId, this.modifyinvoice).then((res) => {
            if (res.data.code === 0) {
              this.modifyinvoice = this.initModifyinvoice
              this.$refs[formName].resetFields()
              this.$message({
                type: 'success',
                message: '操作成功'
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
    /* 搜索 */
    searchBtn () {
      this.currentPage = 1
      this.getDatalist()
    }
  },
  watch: {
    selectvalue () {
      this.datalist = []
      this.currentPage = 1
      this.getDatalist()
    },
    /* 发票类型搜索 */
    invoicetype () {
      this.datalist = []
      this.currentPage = 1
      this.getDatalist()
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.invoiceExamine
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
      width: 200px;
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
      width: 200px;
</style>
