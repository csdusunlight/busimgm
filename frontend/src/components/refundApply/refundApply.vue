<template>
  <div class="refundAdmin">
    <el-row>
      <el-col :span="22">
        <div class="input_search">
          <div class="search margin_clear search_box">
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
          <div class="select" style="margin-left: 15px;">
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
      <el-col :span="2">
        <div class="flexright">
          <el-button size="medium" type="primary">搜索</el-button>
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
                <el-radio :label="0">否</el-radio>
                <el-radio :label="1">是</el-radio>
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
  </div>
</template>

<script>
import {examineOption, paccounOption} from '@/common/js/options'
import {postRefund, allGetProject, getRefundList} from '@/api/api'
export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      inputdate2: '',
      inputdate3: '',
      projectname: '',
      takeover: '',
      contractcop: '',
      examinestate: '0',
      options: examineOption,
      paccountypeops: paccounOption,
      projectOption: [],
      dialogVisible: false,
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
      }
    }
  },
  methods: {
    /* 打开退款申请对话框 */
    newaddRefund () {
      this.dialogVisible = true
    },
    /* 退款申请列表 */
    getRefundDatalist () {
      let data = this.conditionDate()
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
          state: this.selectvalue
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
                message: '新建项目成功!'
              })
              this.dialogVisible = false
              this.getProjectdata()
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
    }
  },
  mounted () {
    this.getProjectList()
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
