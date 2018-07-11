<template>
  <div class="refundAdmin">
    <el-row>
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
            <label class="labeltext">签约公司</label>
            <el-input size="medium" v-model="contractcop"></el-input>
          </div>
          <div class="search marginvi">
            <label class="labeltext">是否开票</label>
            <el-select size="medium" v-model="invoicetype" placeholder="请选择">
              <el-option
                v-for="item in invoiceYesNo"
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
          <div class="select" style="margin-left: 20px;">
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
          <el-button size="medium" @click="newaddRefund()" type="info">退款申请</el-button>
        </div>
      </el-col>
      <el-dialog
        title="退款申请"
        :visible.sync="dialogVisible"
        width="50%"
        >
        <div class="form_table">
          <el-form :model="addRefund" :rules="rules" ref="addRefund" label-width="120px" class="demo-ruleForm">
            <el-form-item label="项目名称" prop="project">
              <el-select size="medium" filterable v-model="addRefund.project" placeholder="请选择">
                <el-option
                  v-for="item in projectOption"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="company">
              <el-input v-model="addRefund.company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="平台名称" prop="platname">
              <el-input v-model="addRefund.platname" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="对公对私" prop="fundtype">
              <el-select size="medium" v-model="addRefund.fundtype" placeholder="请选择">
                <el-option
                  v-for="item in paccountypeops"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="是否已开票" prop="is_invoice">
              <el-radio-group v-model="addRefund.is_invoice">
                <el-radio :label="0">是</el-radio>
                <el-radio :label="1">否</el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="预付款金额" prop="inprest">
              <el-input v-model="addRefund.inprest" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="已消耗金额" prop="consume_sum">
              <el-input v-model="addRefund.consume_sum" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="退款金额" prop="refund_rec">
              <el-input v-model="addRefund.refund_rec" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="签约公司" prop="contract_company">
              <el-input v-model="addRefund.contract_company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开户行" prop="bank">
              <el-input v-model="addRefund.bank" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="银行账号" prop="bank_account">
              <el-input v-model="addRefund.bank_account" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="退款原因" prop="refund_reason">
              <el-input type="textarea" v-model="addRefund.refund_reason" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="subPostRefund('addRefund')">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.results" style="width: 100%">
          <el-table-column label="日期" prop="apply_date" width="100"></el-table-column>
          <el-table-column label="项目名称" prop="projectname"></el-table-column>
          <el-table-column label="甲方公司名称" prop="company"></el-table-column>
          <el-table-column label="平台名称" prop="platname" width="100"></el-table-column>
          <el-table-column label="对公对私">
            <template slot-scope="scope">
              <span>{{paccountFliter[scope.row.fundtype]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="是否已开票">
            <template slot-scope="scope">
              <span>{{invoiceFilter[scope.row.is_invoice]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="预付款金额" prop="inprest" width="100"></el-table-column>
          <el-table-column label="已消耗金额" prop="consume_sum"></el-table-column>
          <el-table-column label="退款金额" prop="refund_rec"></el-table-column>
          <el-table-column label="签约公司" prop="contract_company"></el-table-column>
          <el-table-column label="开户行" prop="bank"></el-table-column>、
          <el-table-column label="银行账号" prop="bank_account"></el-table-column>
          <el-table-column label="退款原因" prop="refund_reason"></el-table-column>
          <el-table-column label="审核状态" prop="state">
            <template slot-scope="scope">
              <span>{{stateFilter[scope.row.state]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作" v-if="operationShow">
            <template slot-scope="scope">
              <div class="operation_button">
                <div class="op_button_padding"><el-button size="mini" type="danger" @click="modifyRefundBtn(scope.row)">修改</el-button></div>
                <div class="op_button_padding"><el-button size="mini" type="warning" @click="deleteRefundBtn(scope.row)">删除</el-button></div>
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
        title="退款申请修改"
        :visible.sync="modifyRefundVisible"
        width="50%"
        >
        <div class="form_table">
          <el-form :model="modifyRefund" ref="addRefund" label-width="120px" class="demo-ruleForm">
            <el-form-item label="项目名称" prop="project">
              <el-select size="medium" filterable v-model="modifyRefund.project" placeholder="请选择">
                <el-option
                  v-for="item in projectOption"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="company">
              <el-input v-model="modifyRefund.company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="平台名称" prop="platname">
              <el-input v-model="modifyRefund.platname" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="对公对私" prop="fundtype">
              <el-select size="medium" v-model="modifyRefund.fundtype" placeholder="请选择">
                <el-option
                  v-for="item in paccountypeops"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="是否已开票" prop="is_invoice">
              <el-radio v-model="modifyRefund.is_invoice" label="0">是</el-radio>
              <el-radio v-model="modifyRefund.is_invoice" label="1">否</el-radio>
            </el-form-item>
            <el-form-item label="预付款金额" prop="inprest">
              <el-input v-model="modifyRefund.inprest" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="已消耗金额" prop="consume_sum">
              <el-input v-model="modifyRefund.consume_sum" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="退款金额" prop="refund_rec">
              <el-input v-model="modifyRefund.refund_rec" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="签约公司" prop="contract_company">
              <el-input v-model="modifyRefund.contract_company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开户行" prop="bank">
              <el-input v-model="modifyRefund.bank" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="银行账号" prop="bank_account">
              <el-input v-model="modifyRefund.bank_account" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="退款原因" prop="refund_reason">
              <el-input type="textarea" v-model="modifyRefund.refund_reason" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="subModifyRefund">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
  </div>
</template>

<script>
import {examineOption, paccounOption, paccountypeopsFilter, examineFilter} from '@/common/js/options'
import {postRefund, allGetProject, getRefundList, putRefund, deleteRefund} from '@/api/api'
export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      projectname: '',
      contractcop: '',
      invoicetype: '',
      fundtypevalue: '',
      examinestate: '0',
      options: examineOption,
      paccountypeops: paccounOption,
      paccountFliter: paccountypeopsFilter,
      stateFilter: examineFilter,
      projectOption: [],
      dialogVisible: false,
      modifyRefundVisible: false,
      operationShow: true,
      invoiceFilter: {0: '是', 1: '否'},
      loading: true,
      dataList: {},
      currentPage: 1,
      invoiceYesNo: [
        {
          value: '',
          label: '全部'
        },
        {
          value: '0',
          label: '是'
        },
        {
          value: '1',
          label: '否'
        }
      ],
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
      addRefund: {
        project: '',
        company: '',
        platname: '',
        fundtype: '',
        is_invoice: '',
        inprest: '',
        consume_sum: '',
        refund_rec: '',
        contract_company: '',
        bank: '',
        bank_account: '',
        refund_reason: ''
      },
      initAddRefund: {
        project: '',
        company: '',
        platname: '',
        fundtype: '',
        is_invoice: '',
        inprest: '',
        consume_sum: '',
        refund_rec: '',
        contract_company: '',
        bank: '',
        bank_account: '',
        refund_reason: ''
      },
      rules: {
        project: [
          { required: true, message: '选择项目', trigger: 'blur' }
        ],
        company: [
          { required: true, message: '请输入甲方公司公司', trigger: 'blur' }
        ],
        platname: [
          { required: true, message: '请输入平台名称', trigger: 'blur' }
        ],
        fundtype: [
          { required: true, message: '请选择公私', trigger: 'blur' }
        ],
        is_invoice: [
          { required: true, message: '是否已开票', trigger: 'blur' }
        ],
        inprest: [
          { required: true, message: '请输入预付款金额', trigger: 'blur' }
        ],
        consume_sum: [
          { required: true, message: '请输入已消耗金额', trigger: 'blur' }
        ],
        refund_rec: [
          { required: true, message: '请输入退款金额', trigger: 'blur' }
        ],
        contract_company: [
          { required: true, message: '请输入签约公司', trigger: 'blur' }
        ],
        bank: [
          { required: true, message: '请输入开户行', trigger: 'blur' }
        ],
        bank_account: [
          { required: true, message: '请输入银行账号', trigger: 'blur' }
        ],
        refund_reason: [
          { required: true, message: '请输入退款原因', trigger: 'blur' }
        ]
      },
      modifyRefund: {
        fundtype: '',
        project: '',
        is_invoice: ''
      }
    }
  },
  created () {
    this.getRefundDatalist()
  },
  methods: {
    /* 打开退款申请对话框 */
    newaddRefund () {
      this.dialogVisible = true
    },
    /* 退款申请列表 */
    getRefundDatalist () {
      let data = this.conditionDate()
      if (this.examinestate === '0') {
        this.operationShow = true
      } else {
        this.operationShow = false
      }
      getRefundList(this.currentPage, data).then((res) => {
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
          projectname: this.projectname,
          contract_company: this.contractcop,
          state: this.examinestate,
          is_invoice: this.invoicetype,
          fundtype: this.fundtypevalue
        }
      }
      return Data
    },
    /* 提交退款申请 */
    subPostRefund (addRefund) {
      this.$refs[addRefund].validate((valid) => {
        if (valid) {
          postRefund(this.addRefund).then((res) => {
            if (res.data.code === 0) {
              this.addRefund = this.initAddRefund
              this.$refs[addRefund].resetFields()
              this.$message({
                type: 'success',
                message: '提交退款申请成功'
              })
              this.dialogVisible = false
              this.loading = true
              this.getRefundDatalist()
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
      this.datalist = []
      this.loading = true
      this.currentPage = val
      this.getRefundDatalist()
    },
    /* 打开修改退款申请对话框 */
    modifyRefundBtn (row) {
      this.modifyRefundVisible = true
      Object.assign(this.modifyRefund, row)
      console.log(this.modifyRefund)
    },
    /* 提交退款修改 */
    subModifyRefund () {
      putRefund(this.modifyRefund.id, this.modifyRefund).then((res) => {
        console.log(res)
        this.$message({
          type: 'success',
          message: '修改成功!'
        })
        this.modifyRefundVisible = false
        this.loading = true
        this.getRefundDatalist()
      }).catch((err) => {
        this.modifyRefundVisible = false
        console.log(err)
      })
    },
    /* 删除退款申请 */
    deleteRefundBtn (row) {
      this.$confirm('此操作将永久删除该申请, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteRefund(row.id).then((res) => {
          if (res.data.code === 0) {
            this.$message({
              type: 'success',
              message: '删除成功!'
            })
            this.loading = true
            this.getRefundDatalist()
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
      this.loading = true
      this.currentPage = 1
      this.getRefundDatalist()
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
      this.getRefundDatalist()
    },
    /* 是否开票搜索 */
    invoicetype () {
      this.dataList = []
      this.loading = true
      this.currentPage = 1
      this.getRefundDatalist()
    },
    /* 对公对私搜索 */
    fundtypevalue () {
      this.dataList = []
      this.loading = true
      this.currentPage = 1
      this.getRefundDatalist()
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.refundAdmin
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
  .select
    .label
      margin-right: 10px;
    .el-select, .el-select--medium
      width: 170px;
  .flexright
    display: flex;
    justify-content: flex-end;
  .marginvi
    margin-left: 0;
</style>
