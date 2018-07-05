<template>
  <div class="projectAdmin">
    <el-row>
      <el-col :span="24">
        <div class="input_search">
          <div class="search marginvi search_box">
            <label class="labeltext">立项日期</label>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate0" size="medium" type="date" placeholder="选择日期"></el-date-picker>
            <span class="line"> — </span>
            <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate1" size="medium" type="date" placeholder="选择日期"></el-date-picker>
          </div>
          <div class="search">
            <label class="labeltext">项目编号</label>
            <el-input size="medium" v-model="projectnum"></el-input>
          </div>
          <div class="search">
            <label class="labeltext">项目名称</label>
            <el-input size="medium" v-model="projectname"></el-input>
          </div>
          <div class="search">
            <label class="labeltext">商务对接人</label>
            <el-input size="medium" v-model="takeover"></el-input>
          </div>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top">
      <el-col :span="20">
        <div class="flex_default">
          <div class="search marginvi inputmaxwidth">
            <label class="labeltext">签约公司</label>
            <el-input size="medium" v-model="signingCp"></el-input>
          </div>
          <div class="select margin_left">
            <label class="label">结算方式</label>
            <el-select size="medium" v-model="settlement" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </div>
          <div class="select margin_left">
            <label class="label">项目状态</label>
            <el-select size="medium" v-model="projectstate" placeholder="请选择">
              <el-option
                v-for="item in proOptions"
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
          <el-button size="medium" @click="newAddproject()" type="info">新增项目</el-button>
        </div>
      </el-col>
      <el-dialog
        title="项目申请"
        :visible.sync="dialogVisible"
        width="50%"
        >
        <div class="form_table">
          <el-form :model="addProject" :rules="rules" ref="addProject" label-width="120px" class="demo-ruleForm">
            <el-form-item label="项目名称" prop="name">
              <el-input v-model="addProject.name" size="medium" placeholder="平台名称+日期，如：钱宝宝180601"></el-input>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="company">
              <el-input v-model="addProject.company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="平台名称" prop="platname">
              <el-input v-model="addProject.platname" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="对公对私" prop="paccountype">
              <el-select size="medium" v-model="addProject.paccountype" placeholder="请选择">
                <el-option
                  v-for="item in paccountypeops"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="结算方式" prop="settleway">
              <el-select size="medium" v-model="addProject.settleway" placeholder="请选择">
                <el-option
                  v-for="item in settlewayops"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="签约公司" prop="contract_company">
              <el-input v-model="addProject.contract_company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="结算详情" prop="settle_detail">
              <el-input v-model="addProject.settle_detail" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="合作详情" prop="pcoperatedetail">
              <el-input v-model="addProject.pcoperatedetail" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="备注">
              <el-input type="textarea" v-model="addProject.remark" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="subPostProject('addProject')">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.results" style="width: 100%">
          <el-table-column label="项目编号" prop="id"></el-table-column>
          <el-table-column label="日期" prop="lanched_apply_date"></el-table-column>
          <el-table-column label="项目名称" prop="name"></el-table-column>
          <el-table-column label="项目状态" prop="state">
            <template slot-scope="scope">
              <span v-if="scope.row.state !== '5' && scope.row.state !== '6'">{{stateFilter[scope.row.state]}}</span>
              <span class="cursou" @click="clickthcout" v-else-if="scope.row.state === '6'">{{stateFilter[scope.row.state]}}</span>
              <span class="cursou" @click="clickthcout" v-else>{{stateFilter[scope.row.state]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="结项日期" prop="concluded_audit_date"></el-table-column>
          <el-table-column label="消耗费用" prop="consume"></el-table-column>
          <el-table-column label="已结算费用" prop="settle" width="95"></el-table-column>
          <el-table-column label="待结算/消耗费用" prop="topay_amount"></el-table-column>
          <el-table-column label="已开票金额" prop="invoicenum"></el-table-column>
          <el-table-column label="备注" prop="remark"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <div class="operation_button">
                <div class="op_button_padding"><el-button size="mini" type="primary" @click="lookProject(scope.row)">查看</el-button></div>
                <div class="op_button_padding" v-if="scope.row.state === '0' || scope.row.state === '1'"><el-button size="mini" type="danger" @click="modifyproject(scope.row)">修改</el-button></div>
                <div class="op_button_padding" v-if="scope.row.state === '0'"><el-button size="mini" type="warning" @click="deleteProjectBtn(scope.row)">删除</el-button></div>
                <div class="op_button_padding" v-if="scope.row.state === '1'"><el-button size="mini" type="success" @click="junctions(scope.row)">结项</el-button></div>
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
      <el-dialog title="项目数据" :visible.sync="lookProjectTable" width="70%">
        <div class="table-list">
          <el-table :data="detailsList.results" style="width: 100%" @row-click='handleRowHandle'>
            <el-table-column label="日期" prop="lanched_apply_date"></el-table-column>
            <el-table-column label="项目名称" prop="name"></el-table-column>
            <el-table-column label="投资人数" prop="state"></el-table-column>
            <el-table-column label="投资金额" prop="concluded_date"></el-table-column>
            <el-table-column label="消耗费用" prop="consume"></el-table-column>
            <el-table-column label="返现投资人数" prop="settle" width="95"></el-table-column>
            <el-table-column label="返现投资金额" prop="topay_amount"></el-table-column>
            <el-table-column label="返现费用" prop="invoicenum"></el-table-column>
          </el-table>
        </div>
        <div class="pagination">
          <el-pagination
            background
            @current-change="detailsCurrentChange"
            :page-size="10"
            :current-page="this.detailsCurrentPage"
            layout="prev, pager, next, total, jumper"
            :total="this.detailsList.recordCount">
          </el-pagination>
        </div>
      </el-dialog>
      <el-dialog title="项目修改" :visible.sync="modifyProjectfrom" width="50%">
        <div class="form_table">
          <el-form :model="modifyProject"  ref="modifyProject" label-width="120px" class="demo-ruleForm">
            <el-form-item label="项目名称">
              <el-input v-model="modifyProject.name" size="medium" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="甲方公司名称" prop="company">
              <el-input v-model="modifyProject.company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="平台名称" prop="platname">
              <el-input v-model="modifyProject.platname" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="对公对私" prop="paccountype">
              <el-select size="medium" v-model="modifyProject.paccountype" placeholder="请选择">
                <el-option
                  v-for="item in paccountypeops"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="结算方式" prop="settleway">
              <el-select size="medium" v-model="modifyProject.settleway" placeholder="请选择">
                <el-option
                  v-for="item in settlewayops"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="签约公司" prop="contract_company">
              <el-input v-model="modifyProject.contract_company" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="结算详情" prop="settle_detail">
              <el-input v-model="modifyProject.settle_detail" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="合作详情" prop="pcoperatedetail">
              <el-input v-model="modifyProject.pcoperatedetail" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="备注">
              <el-input type="textarea" v-model="modifyProject.remark" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="modifyProjectfrom = false">取 消</el-button>
          <el-button type="primary" @click="subModiftProject('modifyProject')">确 定</el-button>
        </span>
      </el-dialog>
      <el-dialog title="结项详情" :visible.sync="stateOver" width="30%">
        <ul class="stateover">
          <li><label>项目成本：</label><i>8156.00</i></li>
          <li><label>成本备注：</label><i>游泳健身了解一下撩妹套路了解一下</i></li>
          <li><label>项目毛利：</label><i>741.52</i></li>
        </ul>
      </el-dialog>
      <el-dialog title="结项" :visible.sync="junctionsVisible" width="30%">
        <div class="form_table">
          <el-form :model="addJunctions"  ref="addJunctions" label-width="120px" class="demo-ruleForm">
            <el-form-item label="结算详情" prop="settle_detail">
              <el-input v-model="addJunctions.settle_detail" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="合作详情" prop="pcoperatedetail">
              <el-input v-model="addJunctions.pcoperatedetail" size="medium"></el-input>
            </el-form-item>
            <el-form-item label="备注">
              <el-input type="textarea" v-model="addJunctions.remark" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="junctionsVisible = false">取 消</el-button>
          <el-button type="primary" @click="subJunctionsProject('addJunctions')">确 定</el-button>
        </span>
      </el-dialog>
    </el-row>
  </div>
</template>

<script>
import {postNewProject, getProjectList, getprojectDetails, deleteProject, putProject, endProjectApply} from '@/api/api'
import {paccounOption, settlewayopsoption} from '@/common/js/options'

export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      projectnum: '',
      projectname: '',
      takeover: '',
      signingCp: '',
      settlement: '',
      projectstate: '0',
      examinestate: '0',
      dataList: '',
      detailsList: '',
      dialogVisible: false,
      lookProjectTable: false,
      stateOver: false,
      modifyProjectfrom: false,
      junctionsVisible: false,
      currentPage: 1,
      detailsCurrentPage: 1,
      loading: true,
      stateOperation: '',
      searchDetailsName: '',
      searchState: 0,
      addProject: {
        name: '',
        company: '',
        platname: '',
        paccountype: '',
        settleway: '',
        contract_company: '',
        contact: '',
        settle_detail: '',
        pcoperatedetail: ''
      },
      initAddProject: {
        name: '',
        company: '',
        platname: '',
        paccountype: '',
        settleway: '',
        contract_company: '',
        contact: '',
        settle_detail: '',
        pcoperatedetail: '',
        remark: ''
      },
      rules: {
        name: [
          { required: true, message: '请输入项目名称', trigger: 'blur' }
        ],
        company: [
          { required: true, message: '请输入甲方公司名称', trigger: 'blur' }
        ],
        platname: [
          { required: true, message: '请输入平台名称', trigger: 'blur' }
        ],
        paccountype: [
          { required: true, message: '请选择对公对私', trigger: 'blur' }
        ],
        settleway: [
          { required: true, message: '请选择结算方式', trigger: 'blur' }
        ],
        contract_company: [
          { required: true, message: '请输入签约公司', trigger: 'blur' }
        ],
        settle_detail: [
          { required: true, message: '请输入结算详情', trigger: 'blur' }
        ],
        contact: [
          { required: true, message: '请输入商务对接人', trigger: 'blur' }
        ],
        pcoperatedetail: [
          { required: true, message: '请输入合作详情', trigger: 'blur' }
        ]
      },
      addJunctions: {
        settle_detail: '',
        pcoperatedetail: '',
        remark: ''
      },
      projectId: '',
      options: [
        {
          value: '',
          label: '全部'
        },
        {
          value: '0',
          label: '预付款'
        },
        {
          value: '1',
          label: '后付款'
        }
      ],
      proOptions: [
        {
          value: '0',
          label: '待审核'
        },
        {
          value: '1',
          label: '进行中'
        },
        {
          value: '2',
          label: '审核未通过'
        },
        {
          value: '4',
          label: '结项中'
        },
        {
          value: '5',
          label: '已结项'
        },
        {
          value: '6',
          label: '结项失败'
        }
      ],
      stateFilter: {0: '待审核', 1: '进行中', 2: '审核未通过', 4: '结项中', 5: '已结项', 6: '结项失败'},
      settlewayops: settlewayopsoption,
      paccountypeops: paccounOption,
      modifyProject: {
        paccountype: '',
        settleway: ''
      }
    }
  },
  created () {
    this.getProjectdata()
  },
  methods: {
    /* 打开新建项目 */
    newAddproject () {
      this.dialogVisible = true
    },
    /* 获取项目列表 */
    getProjectdata () {
      let data = this.conditionDate()
      getProjectList(this.currentPage, data).then((res) => {
        console.log(res)
        this.dataList = res.data
        this.loading = false
        if (res.code) {
        } else {
          /* this.$message(res.data.detail) */
        }
      }).catch((err) => {
        console.log('error')
        console.log(err)
      })
    },
    /* 搜索条件拼接 */
    conditionDate () {
      let Data = {
        params: {
          lanched_apply_date_0: this.inputdate0,
          lanched_apply_date_1: this.inputdate1,
          id: this.projectnum,
          name: this.projectname,
          contact: this.takeover,
          contract_company: this.signingCp,
          settleway: this.settlement,
          state: this.projectstate
        }
      }
      return Data
    },
    /* 提交新建项目 */
    subPostProject (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          postNewProject(this.addProject).then((res) => {
            if (res.data.code === 0) {
              this.addProject = this.initAddProject
              this.$refs[formName].resetFields()
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
    /* 分页 */
    handleCurrentChange (val) {
      this.loading = true
      this.currentPage = val
      this.getProjectdata()
    },
    /* 打开项目修改对话框 */
    modifyproject (row) {
      this.modifyProjectfrom = true
      Object.assign(this.modifyProject, row)
    },
    /* 详情搜索 */
    getDetailsList (data) {
      getprojectDetails(this.detailsCurrentPage, data).then((res) => {
        console.log(res)
        this.detailsList = res.data
      })
    },
    /* 点击查看按钮详情 */
    lookProject (row) {
      this.searchDetailsName = row.name
      this.getDetailsList(this.searchDetailsName)
      this.lookProjectTable = true
    },
    /* 点击 行 查看详情 */
    handleRowHandle (val) {
      this.searchDetailsName = val.name
      this.getDetailsList(this.searchDetailsName)
      this.lookProjectTable = true
    },
    /* 详情分页 */
    detailsCurrentChange (val) {
      this.detailsCurrentPage = val
      this.getDetailsList(this.searchDetailsName)
    },
    /* 已结项详情 */
    clickthcout () {
      this.stateOver = true
    },
    /* 提交修改项目 */
    subModiftProject () {
      putProject(this.modifyProject.id, this.modifyProject).then((res) => {
        console.log(res)
        this.$message({
          type: 'success',
          message: '修改成功!'
        })
        this.modifyProjectfrom = false
        this.getProjectdata()
      }).catch((err) => {
        this.modifyProjectfrom = false
        console.log(err)
      })
    },
    /* 删除项目 */
    deleteProjectBtn (row) {
      this.$confirm('此操作将永久删除该项目, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        deleteProject(row.id).then((res) => {
          console.log(res)
          this.$message({
            type: 'success',
            message: '删除成功!'
          })
          this.getProjectdata()
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    /* 结项 */
    junctions (row) {
      this.projectId = row.id
      this.junctionsVisible = true
    },
    /* 提交结项内容 */
    subJunctionsProject () {
      console.log(this.addJunctions)
      endProjectApply(this.projectId, this.addJunctions).then((res) => {
        if (res.code === '0') {
          this.$message({
            type: 'success',
            message: '操作成功!'
          })
        } else {
          this.$message({
            type: 'error',
            message: res.detail
          })
        }
      })
    },
    /* 搜索 */
    searchBtn () {
      this.currentPage = 1
      this.getProjectdata()
    }
  },
  watch: {
    settlement () {
      this.currentPage = 1
      this.getProjectdata()
    },
    projectstate () {
      this.currentPage = 1
      this.getProjectdata()
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
.projectAdmin
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
      width: 145px;
    .el-input
      width: 150px;
  .select
    .label
      margin-right: 10px;
    .el-select, .el-select--medium
      width: 160px;
  .inputmaxwidth
    .el-input
      width: 200px;
  .marginvi
    margin-left: 0;
  .flexright
    display: flex;
    justify-content: flex-end;
  .cursou
    cursor: pointer;
    text-decoration: underline;
  .stateover
    li
      padding: 10px 0;
</style>
