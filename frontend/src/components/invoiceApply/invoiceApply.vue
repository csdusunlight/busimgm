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
            <el-input size="medium" v-model="invoicetype"></el-input>
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
          <el-button size="medium" type="primary">搜索</el-button>
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
            <el-form-item label="项目名称" prop="resource">
            <el-select size="medium" v-model="invoice.resource" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
            </el-form-item>
            <el-form-item label="发票类型" prop="resource">
              <el-radio-group v-model="invoice.resource">
                <el-radio label="专票"></el-radio>
                <el-radio label="普票"></el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="返现金额" prop="resource">
              <el-input v-model="invoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开票日期">
              <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="invoice.resource" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            </el-form-item>
            <el-form-item label="签约公司" prop="resource">
              <el-input v-model="invoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="resource">
              <el-input v-model="invoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="纳税人识别号" prop="resource">
              <el-input v-model="invoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="注册地址" prop="resource">
              <el-input v-model="invoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="银行账号" prop="resource">
              <el-input v-model="invoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开户行" prop="resource">
              <el-input v-model="invoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="电话" prop="resource">
              <el-input v-model="invoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开票金额" prop="resource">
              <el-input v-model="invoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="resource">
              <el-input type="textarea" v-model="invoice.resource" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.data" style="width: 100%" @sort-change="sortChange">
          <el-table-column label="日期" prop="date" sortable="custom" width="100"></el-table-column>
          <el-table-column label="项目名称" prop="string"></el-table-column>
          <el-table-column label="开票日期" prop="integer"></el-table-column>
          <el-table-column label="发票类型" prop="integer"></el-table-column>
          <el-table-column label="签约公司" prop="qq_number" width="100"></el-table-column>
          <el-table-column label="甲方公司名称" prop="float"></el-table-column>
          <el-table-column label="开票金额" prop="integer"></el-table-column>
          <el-table-column label="审核状态" prop="integer"></el-table-column>
          <el-table-column label="备注" prop="integer"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <div class="operation_button">
                <div class="op_button_padding"><el-button size="mini" type="danger" @click="opInvoice(scope.row)">修改</el-button></div>
                <div class="op_button_padding"><el-button size="mini" type="warning" @click="opInvoice(scope.row)">删除</el-button></div>
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
          :total="this.dataList.total">
        </el-pagination>
      </div>
      <el-dialog
        title="发票修改"
        :visible.sync="invoiceVisible"
        width="50%"
        >
        <div class="form_table">
          <el-form :model="mdyInvoice" :rules="mdyrules" ref="mdyInvoice" label-width="120px" class="demo-ruleForm">
            <el-form-item label="项目名称" prop="resource">
            <el-select size="medium" v-model="mdyInvoice.resource" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
            </el-form-item>
            <el-form-item label="发票类型" prop="resource">
              <el-radio-group v-model="mdyInvoice.resource">
                <el-radio label="专票"></el-radio>
                <el-radio label="普票"></el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="返现金额" prop="resource">
              <el-input v-model="mdyInvoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开票日期">
              <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="mdyInvoice.resource" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            </el-form-item>
            <el-form-item label="签约公司" prop="resource">
              <el-input v-model="mdyInvoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="resource">
              <el-input v-model="mdyInvoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="纳税人识别号" prop="resource">
              <el-input v-model="mdyInvoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="注册地址" prop="resource">
              <el-input v-model="mdyInvoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="银行账号" prop="resource">
              <el-input v-model="mdyInvoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开户行" prop="resource">
              <el-input v-model="mdyInvoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="电话" prop="resource">
              <el-input v-model="mdyInvoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="开票金额" prop="resource">
              <el-input v-model="mdyInvoice.resource" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="备注" prop="resource">
              <el-input type="textarea" v-model="mdyInvoice.resource" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="invoiceVisible = false">取 消</el-button>
          <el-button type="primary" @click="invoiceVisible = false">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
  </div>
</template>

<script>
import {examineOption} from '@/common/js/options'
import {dataPage} from '@/api/api'

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
      currentPage: 1,
      dataList: [],
      param: {
        page: 1
      },
      invoice: {
        resource: ''
      },
      rules: {
        resource: [
          { required: true, message: '项目名称', trigger: 'blur' }
        ]
      },
      mdyInvoice: {
        resource: ''
      },
      mdyrules: {
        resource: [
          { required: true, message: '项目名称', trigger: 'blur' }
        ]
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
    getDatalist () {
      dataPage(this.param).then((res) => {
        console.log(res)
        this.dataList = res.data
        this.loading = false
      }).catch((err) => {
        console.log(err)
      })
    },
    handleCurrentChange (val) {
      this.datalist = []
      this.loading = true
      this.currentPage = val
      this.param.page = val
      this.getDatalist()
    },
    sortChange (val) {
      console.log(val)
    },
    opInvoice (row) {
      this.invoiceVisible = true
      console.log(row)
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
