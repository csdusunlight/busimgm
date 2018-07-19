<template>
  <div class="projectAdmin">
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="立项审核" name="first">
        <div>
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
                  <label class="labeltext">项目名称</label>
                  <el-input size="medium" v-model="projectname"></el-input>
                </div>
                <div class="search">
                  <label class="labeltext">商务对接人</label>
                  <el-input size="medium" v-model="takeover"></el-input>
                </div>
                <div class="search marginvi">
                  <label class="labeltext">签约公司</label>
                  <el-input size="medium" v-model="signingCp"></el-input>
                </div>
              </div>
            </el-col>
          </el-row>
          <el-row class="row_top">
            <el-col :span="20">
              <div class="flex_default">
                <div class="search marginvi search_box">
                  <label class="labeltext">审核日期</label>
                  <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate2" size="medium" type="date" placeholder="选择日期"></el-date-picker>
                  <span class="line"> — </span>
                  <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate3" size="medium" type="date" placeholder="选择日期"></el-date-picker>
                </div>
                <div class="select margin_left">
                  <label class="label">结算方式</label>
                  <el-select size="medium" v-model="settlement" placeholder="请选择">
                    <el-option
                      v-for="item in settleOptions"
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
                <el-button @click="searchData" size="medium" type="primary">搜索</el-button>
              </div>
            </el-col>
          </el-row>
        </div>
        <div class="table-list row_top row_bottom">
          <el-table v-loading="loading" :data="dataList.results" style="width: 100%">
            <el-table-column label="项目编号" prop="id"></el-table-column>
            <el-table-column label="日期" prop="lanched_apply_date"></el-table-column>
            <el-table-column label="项目名称" prop="name"></el-table-column>
            <el-table-column label="甲方公司名称" prop="company"></el-table-column>
            <el-table-column label="平台名称" prop="platname"></el-table-column>
            <el-table-column label="商务对接人" prop="contact"></el-table-column>
            <el-table-column label="对公对私">
              <template slot-scope="scope">
                <span>{{paccountFliter[scope.row.paccountype]}}</span>
              </template>
            </el-table-column>
            <el-table-column label="结算方式" prop="settleway_des"></el-table-column>
            <el-table-column label="签约公司" prop="contract_company"></el-table-column>
            <el-table-column label="结算详情" prop="settle_detail"></el-table-column>
            <el-table-column label="合作详情" prop="pcoperatedetail"></el-table-column>
            <el-table-column label="审核人" prop="audituser" :key="Math.random()" v-if="examineData"></el-table-column>
            <el-table-column label="审核时间" prop="lanched_audit_date" :key="Math.random()" v-if="examineData"></el-table-column>
            <el-table-column label="拒绝原因" prop="lanched_refused_reason" :key="Math.random()" v-if="examineAdopt"></el-table-column>
            <el-table-column label="备注" prop="remark"></el-table-column>
            <el-table-column
              v-if = "projectstate == '0'"
              :key="Math.random()"
              label="操作">
              <template slot-scope="scope">
                <div class="operation_button">
                  <div class="op_button_padding"><el-button size="mini" type="warning" @click="comfirmProjectAdd(scope.row.id)">审核</el-button></div>
                  <div class="op_button_padding"><el-button size="mini" type="success" @click="refuseProjectAdd(scope.row.id)">拒绝</el-button></div>
                </div>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="pagination">
          <el-pagination
            background
            @current-change="pageChange"
            :page-size="10"
            :current-page="currentPage"
            layout="prev, pager, next, total, jumper"
            :total="dataList.recordCount">
          </el-pagination>
        </div>
      </el-tab-pane>
      <el-tab-pane label="结项审核" name="second">
        <div>
          <el-row>
            <el-col :span="24">
              <div class="input_search">
                <div class="search marginvi search_box">
                  <label class="labeltext">结项日期</label>
                  <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate0_2" size="medium" type="date" placeholder="选择日期"></el-date-picker>
                  <span class="line"> — </span>
                  <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate1_2" size="medium" type="date" placeholder="选择日期"></el-date-picker>
                </div>
                <div class="search">
                  <label class="labeltext">项目名称</label>
                  <el-input size="medium" v-model="projectname_2"></el-input>
                </div>
                <div class="search">
                  <label class="labeltext">商务对接人</label>
                  <el-input size="medium" v-model="takeover_2"></el-input>
                </div>
                <div class="search marginvi">
                  <label class="labeltext">签约公司</label>
                  <el-input size="medium" v-model="signingCp_2"></el-input>
                </div>
              </div>
            </el-col>
          </el-row>
          <el-row class="row_top">
            <el-col :span="20">
              <div class="flex_default">
                <div class="search marginvi search_box">
                  <label class="labeltext">审核日期</label>
                  <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate2_2" size="medium" type="date" placeholder="选择日期"></el-date-picker>
                  <span class="line"> — </span>
                  <el-date-picker format="yyyy-MM-dd" value-format="yyyy-MM-dd" v-model="inputdate3_2" size="medium" type="date" placeholder="选择日期"></el-date-picker>
                </div>
                <div class="select margin_left">
                  <label class="label">结算方式</label>
                  <el-select size="medium" v-model="settlement_2" placeholder="请选择">
                    <el-option
                      v-for="item in settleOptions_2"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                  </el-select>
                </div>
                <div class="select margin_left">
                  <label class="label">项目状态</label>
                  <el-select size="medium" v-model="projectstate_2" placeholder="请选择">
                    <el-option
                      v-for="item in proOptions_2"
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
                <el-button @click="searchData" size="medium" type="primary">搜索</el-button>
              </div>
            </el-col>
          </el-row>
        </div>
        <div class="table-list row_top row_bottom">
          <el-table v-loading="loading" :data="dataList2.results" style="width: 100%">
            <el-table-column label="项目编号" prop="id"></el-table-column>
            <el-table-column label="日期" prop="lanched_apply_date"></el-table-column>
            <el-table-column label="项目名称" prop="name"></el-table-column>
            <el-table-column label="甲方公司名称" prop="company"></el-table-column>
            <el-table-column label="平台名称" prop="platname"></el-table-column>
            <el-table-column label="商务对接人" prop="contact"></el-table-column>
            <el-table-column label="结算金额" prop="settle"></el-table-column>
            <el-table-column label="结项原因" prop="psettlereason"></el-table-column>
            <el-table-column label="备注" prop="remark"></el-table-column>
            <el-table-column
              v-if = "projectstate_2 == '4'"
              :key="Math.random()"
              label="操作">
              <template slot-scope="scope">
                <div class="operation_button">
                  <div class="op_button_padding"><el-button size="mini" type="warning" @click="comfirmProjectEnd(scope.row.id)">审核</el-button></div>
                  <div class="op_button_padding"><el-button size="mini" type="success" @click="refuseProjectEnd(scope.row.id)">拒绝</el-button></div>
                </div>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="pagination">
          <el-pagination
            background
            @current-change="pageChange2"
            :page-size="10"
            :current-page="currentPage2"
            layout="prev, pager, next, total, jumper"
            :total="dataList2.recordCount">
          </el-pagination>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import {getProjectList, addProjectConfirm, addProjectRefuse, endProjectConfirm, endProjectRefuse} from '@/api/api'
import {paccountypeopsFilter} from '@/common/js/options'
export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      projectname: '',
      takeover: '',
      signingCp: '',
      settlement: '',
      examineData: '',
      examineAdopt: '',
      projectstate: '0',
      paccountFliter: paccountypeopsFilter,
      settleOptions: [
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
        }
      ],
      inputdate0_2: '',
      inputdate1_2: '',
      inputdate2_2: '',
      inputdate3_2: '',
      inputdate2: '',
      inputdate3: '',
      projectnum_2: '',
      projectname_2: '',
      takeover_2: '',
      signingCp_2: '',
      settlement_2: '',
      projectstate_2: '4',
      settleOptions_2: [
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
      proOptions_2: [
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
      activeName: 'first',
      dataList: '',
      dataList2: '',
      currentPage: 1,
      currentPage2: 1,
      loading: false
    }
  },
  created () {
    this.getProjectData()
  },
  methods: {
    /* Tab点击 */
    handleClick (tab, event) {
      if (!this.dataList2 && this.activeName === 'second') {
        this.getProjectData()
      }
    },
    /* 分页 */
    pageChange (val) {
      this.loading = true
      this.currentPage = val
      this.getProjectData()
    },
    pageChange2 (val) {
      this.loading = true
      this.currentPage2 = val
      this.getProjectData()
    },
    /* 搜索 */
    searchData () {
      if (this.activeName === 'first') {
        this.currentPage = 1
        this.getProjectData()
      } else if (this.activeName === 'second') {
        this.currentPage2 = 1
        this.getProjectData()
      }
    },
    /* 获取项目列表 */
    getProjectData () {
      let page = 1
      let data = ''
      if (this.projectstate === '0') {
        this.examineData = false
      } else {
        this.examineData = true
      }
      if (this.projectstate === '2') {
        this.examineAdopt = true
      } else {
        this.examineAdopt = false
      }
      if (this.activeName === 'first') {
        page = this.currentPage
        data = this.searchKey
      } else if (this.activeName === 'second') {
        page = this.currentPage2
        data = this.searchKey_2
      }
      getProjectList(page, data).then((res) => {
        if (this.activeName === 'first') {
          this.dataList = res.data
        } else if (this.activeName === 'second') {
          this.dataList2 = res.data
        }
        this.loading = false
      }).catch((err) => {
        console.log(err)
      })
    },
    comfirmProjectAdd (id) {
      this.$confirm('请确认是否审核通过该条数据？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        addProjectConfirm(id).then((res) => {
          if (res.data.code === 0) {
            this.getProjectData()
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
      }).catch((err) => {
        console.log(err)
      })
    },
    refuseProjectAdd (id) {
      this.$prompt('请输入拒绝原因', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        inputPattern: /\S/,
        inputErrorMessage: '请输入拒绝原因'
      }).then(({ value }) => {
        var data = {
          reason: value
        }
        addProjectRefuse(id, data).then((res) => {
          if (res.data.code === 0) {
            this.getProjectData()
            this.$message({
              type: 'success',
              message: '已拒绝，原因： ' + value
            })
          } else {
            this.$message({
              type: 'error',
              message: res.detail
            })
          }
        })
      }).catch((err) => {
        console.log(err)
      })
    },
    comfirmProjectEnd (id) {
      console.log(id)
      this.$confirm('请确认是否审核通过该条数据？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        endProjectConfirm(id).then((res) => {
          this.getProjectData()
          if (res.data.code === 0) {
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
      }).catch((err) => {
        console.log(err)
      })
    },
    refuseProjectEnd (id) {
      this.$prompt('请输入拒绝原因', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        inputPattern: /\S/,
        inputErrorMessage: '请输入拒绝原因'
      }).then(({ value }) => {
        var data = {
          reason: value
        }
        endProjectRefuse(id, data).then((res) => {
          if (res.data.code === 0) {
            this.getProjectData()
            this.$message({
              type: 'success',
              message: '已拒绝，原因： ' + value
            })
          } else {
            this.$message({
              type: 'error',
              message: res.detail
            })
          }
        })
      }).catch((err) => {
        console.log(err)
      })
    }
  },
  watch: {
    settlement () {
      this.searchData()
    },
    projectstate () {
      this.searchData()
    },
    settlement_2 () {
      this.searchData()
    },
    projectstate_2 () {
      this.searchData()
    }
  },
  computed: {
    searchKey: function () {
      var searchStr = {
        params: {
          lanched_apply_date_0: this.inputdate0,
          lanched_apply_date_1: this.inputdate1,
          lanched_audit_date_0: this.inputdate2,
          lanched_audit_date_1: this.inputdate3,
          name: this.projectname,
          contact: this.takeover,
          contract_company: this.signingCp,
          settleway: this.settlement,
          state: this.projectstate
        }
      }
      return searchStr
    },
    searchKey_2: function () {
      var searchStr = {
        params: {
          concluded_apply_date_0: this.inputdate0_2,
          concluded_apply_date_1: this.inputdate1_2,
          concluded_audit_date_0: this.inputdate2_2,
          concluded_audit_date_1: this.inputdate3_2,
          id: this.projectnum_2,
          name: this.projectname_2,
          contact: this.takeover_2,
          contract_company: this.signingCp_2,
          settleway: this.settlement_2,
          state: this.projectstate_2
        }
      }
      return searchStr
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
  .inputmaxwidth
    .el-input
      width: 200px;
  .marginvi
    margin-left: 0;
  .flexright
    display: flex;
    justify-content: flex-end;
</style>
