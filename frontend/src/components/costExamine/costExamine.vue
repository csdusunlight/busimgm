<template>
  <div class="costExamine">
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
            <label class="labeltext">打款时间</label>
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
          <div class="select" style="margin-left: 15px;">
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
          <el-table-column label="打款金额" prop="fund_rec"></el-table-column>
          <el-table-column label="打款时间" prop="send_date"></el-table-column>
          <el-table-column label="打款截图">
            <template slot-scope="scope">
              <div class="img_box" @click="maxPicImage(scope.row.send_pic)">
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
          <el-table-column label="商务对接人" prop="apply_man"></el-table-column>
          <el-table-column label="审核人" prop="audit_man" :key="Math.random()" v-if="examineData"></el-table-column>
          <el-table-column label="审核时间" prop="audit_date" :key="Math.random()" v-if="examineData"></el-table-column>
          <el-table-column label="拒绝原因" prop="audit_refused_reason" :key="Math.random()" v-if="examineAdopt"></el-table-column>
          <el-table-column label="备注" prop="record"></el-table-column>
          <el-table-column label="操作" :key="Math.random()" v-if="operationShow">
            <template slot-scope="scope">
              <div class="operation_button">
                <div class="op_button_padding"><el-button size="mini" type="danger" @click="agreeCostBtn(scope.row)">同意</el-button></div>
                <div class="op_button_padding"><el-button size="mini" type="warning" @click="refuseCostBtn(scope.row)">拒绝</el-button></div>
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
        title="审核拒绝"
        :visible.sync="dialogVisible"
        width="40%"
        >
        <div class="form_table">
          <el-form :model="modifyCost" :rules="rules" ref="modifyCost" label-width="120px" class="demo-modifyCost">
            <el-form-item label="拒绝原因" prop="reason">
              <el-input type="textarea" v-model="modifyCost.reason" size="medium"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="subRefuseCost('modifyCost')">确 定</el-button>
        </span>
      </el-dialog>
      <el-dialog
        title="打款截图"
        :visible.sync="dialogImgShow"
        width="850px"
        >
        <div class="form_table">
          <img :src="imageMax"/>
        </div>
      </el-dialog>
    </el-row>
  </div>
</template>

<script>
import {examineOption, paccountypeopsFilter} from '@/common/js/options'
import {getCostList, agreeCost, refuseCost} from '@/api/api'

export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      inputdate2: '',
      inputdate3: '',
      inputdate4: '',
      inputdate5: '',
      fundtypevalue: '',
      projectname: '',
      onwcopte: '',
      toTakeOver: '',
      auditor: '',
      selectvalue: '0',
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
      options: examineOption,
      dataList: [],
      dialogVisible: false,
      operationShow: true,
      examineData: true,
      examineAdopt: true,
      uploadIcon: false,
      dialogImgShow: false,
      imageMax: '',
      loading: true,
      paccountFliter: paccountypeopsFilter,
      currentPage: 1,
      searchState: 0,
      refuseId: '',
      modifyCost: {
        reason: ''
      },
      initModifyCost: {
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
    this.getCostDatalist()
  },
  methods: {
    /* 费用申请列表 */
    getCostDatalist () {
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
      getCostList(this.currentPage, data).then((res) => {
        this.dataList = res.data
        this.loading = false
      }).catch((err) => {
        console.log(err)
      })
    },
    /* 搜索 */
    searchBtn () {
      this.currentPage = 1
      this.getCostDatalist()
    },
    /* 分页 */
    handleCurrentChange (val) {
      this.loading = true
      this.currentPage = val
      this.getCostDatalist()
    },
    /* 搜索条件拼接 */
    conditionDate () {
      let Data = {
        params: {
          apply_date_0: this.inputdate0,
          apply_date_1: this.inputdate1,
          audit_date_0: this.inputdate2,
          audit_date_1: this.inputdate3,
          send_date_0: this.inputdate4,
          send_date_1: this.inputdate5,
          projectname: this.projectname,
          company: this.onwcopte,
          apply_man: this.toTakeOver,
          audit_man: this.auditor,
          fundtype: this.fundtypevalue,
          state: this.selectvalue
        }
      }
      return Data
    },
    /* 同意操作 */
    agreeCostBtn (row) {
      this.$confirm('请确认是否审核通过该条数据？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        agreeCost(row.id).then((res) => {
          if (res.data.code === 0) {
            this.$message({
              type: 'success',
              message: '操作成功!'
            })
            this.getCostDatalist()
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
    refuseCostBtn (row) {
      this.refuseId = row.id
      this.dialogVisible = true
    },
    /* 提交拒绝原因 */
    subRefuseCost (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          refuseCost(this.refuseId, this.modifyCost).then((res) => {
            if (res.data.code === 0) {
              this.modifyCost = this.initModifyCost
              this.$refs[formName].resetFields()
              this.$message({
                type: 'success',
                message: '操作成功'
              })
              this.loading = true
              this.dialogVisible = false
              this.getCostDatalist()
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
    maxPicImage (row) {
      this.dialogImgShow = true
      this.imageMax = row
    }
  },
  watch: {
    /* 审核状态 */
    selectvalue () {
      this.datalist = []
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
.costExamine
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
    padding-right: 18px;
  .select
    .label
      margin-right: 10px;
    .el-select, .el-select--medium
      width: 200px;
  .search_box
    width: 350px;
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
    cursor: pointer;
    img
      width: 100px
      height: 120px;
  .form_table
    img
      width: 800px;
      height: 500px;
</style>
