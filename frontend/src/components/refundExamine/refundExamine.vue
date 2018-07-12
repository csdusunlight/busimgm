<template>
  <div class="refundExamine">
    <el-row>
      <el-col :span="24">
        <div class="input_search">
          <div class="search marginvi">
            <label class="labeltext">申请日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate0" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate1" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
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
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="24">
        <div class="input_search">
          <div class="search marginvi">
            <label class="labeltext">审核日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate2" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate3" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
          <div class="search">
            <label class="labeltext">审核人</label>
            <el-input size="medium" v-model="auditor"></el-input>
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
          <div class="search marginvi">
            <label class="labeltext">对公对私</label>
            <el-select size="medium" v-model="publicPrivate" placeholder="请选择">
              <el-option
                v-for="item in publicYesNo"
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
          <el-table-column label="商务对接人" prop="apply_man"></el-table-column>
          <el-table-column label="审核人" prop="audit_man" :key="Math.random()" v-if="examineData"></el-table-column>
          <el-table-column label="审核时间" prop="audit_date" :key="Math.random()" v-if="examineData"></el-table-column>
          <el-table-column label="拒绝原因" prop="audit_refused_reason" :key="Math.random()" v-if="examineAdopt"></el-table-column>
          <el-table-column label="操作" v-if="operationShow">
            <template slot-scope="scope">
              <div class="operation_button">
                <div class="op_button_padding"><el-button size="mini" type="danger" @click="AgreeRefundBtn(scope.row)">同意</el-button></div>
                <div class="op_button_padding"><el-button size="mini" type="warning" @click="RefuseRefundBtn(scope.row)">拒绝</el-button></div>
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
          <el-form :model="modifyRefund" :rules="rules" ref="modifyRefund" label-width="120px" class="demo-ruleForm">
            <el-form-item label="拒绝原因" prop="reason">
              <el-input type="textarea" v-model="modifyRefund.reason" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="subRefundRefuse('modifyRefund')">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
  </div>
</template>

<script>
import {getRefundList, agreeRefund, refuseRefund} from '@/api/api'
import {examineOption, paccountypeopsFilter} from '@/common/js/options'
export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      inputdate2: '',
      inputdate3: '',
      projectname: '',
      onwcopte: '',
      toTakeOver: '',
      publicPrivate: '',
      auditor: '',
      selectvalue: '0',
      invoicetype: '',
      examineData: true,
      examineAdopt: true,
      operationShow: true,
      options: examineOption,
      paccountFliter: paccountypeopsFilter,
      dataList: {},
      currentPage: 1,
      refuseId: '',
      loading: true,
      dialogVisible: false,
      publicYesNo: [
        {
          value: '',
          label: '全部'
        },
        {
          value: '0',
          label: '对公'
        },
        {
          value: '1',
          label: '对私'
        }
      ],
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
      invoiceFilter: {0: '是', 1: '否'},
      modifyRefund: {
        reason: ''
      },
      initModifyRefund: {
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
    this.getRefundDatalist()
  },
  methods: {
    /* 退款申请列表 */
    getRefundDatalist () {
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
          audit_date_0: this.inputdate2,
          audit_date_1: this.inputdate3,
          projectname: this.projectname,
          company: this.onwcopte,
          apply_man: this.toTakeOver,
          audit_man: this.auditor,
          is_invoice: this.invoicetype,
          fundtype: this.publicPrivate,
          state: this.selectvalue
        }
      }
      return Data
    },
    /* 分页 */
    handleCurrentChange (val) {
      this.datalist = []
      this.loading = true
      this.currentPage = val
      this.getRefundDatalist()
    },
    /* 同意操作 */
    AgreeRefundBtn (row) {
      this.$confirm('请确认是否审核通过该条数据？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        agreeRefund(row.id).then((res) => {
          if (res.data.code === 0) {
            this.$message({
              type: 'success',
              message: '操作成功!'
            })
            this.getRefundDatalist()
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
    RefuseRefundBtn (row) {
      this.refuseId = row.id
      this.dialogVisible = true
    },
    /* 提交拒绝原因 */
    subRefundRefuse (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          refuseRefund(this.refuseId, this.modifyRefund).then((res) => {
            if (res.data.code === 0) {
              this.modifyRefund = this.initModifyRefund
              this.$refs[formName].resetFields()
              this.$message({
                type: 'success',
                message: '操作成功'
              })
              this.loading = true
              this.dialogVisible = false
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
    /* 搜索 */
    searchBtn () {
      this.loading = true
      this.currentPage = 1
      this.getRefundDatalist()
    }
  },
  watch: {
    /* 审核类型 */
    selectvalue () {
      this.datalist = []
      this.loading = true
      this.currentPage = 1
      this.getRefundDatalist()
    },
    /* 是否开票 */
    invoicetype () {
      this.datalist = []
      this.loading = true
      this.currentPage = 1
      this.getRefundDatalist()
    },
    /* 对公对私 */
    publicPrivate () {
      this.datalist = []
      this.loading = true
      this.currentPage = 1
      this.getRefundDatalist()
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.refundExamine
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
      width: 140px;
    .el-input
      width: 170px;
  .marginvi
    margin-left: 0;
  .flexright
    display: flex;
    justify-content: flex-end;
  .select
    .label
      margin-right: 12px;
</style>
