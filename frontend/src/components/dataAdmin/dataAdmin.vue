<template>
  <div class="dataadmin">
    <el-row>
      <el-col :span="24">
        <div class="input_search">
          <div class="search marginvi search_box">
            <label class="labeltext">立项日期</label>
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
            <el-input size="medium" v-model="projectname"></el-input>
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
            <label class="label">项目状态</label>
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
          <el-button size="medium" type="primary">搜索</el-button>
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
          <el-button size="medium" type="info">导出</el-button>
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
          <el-button size="medium" type="info">获取初始导入模板</el-button>
        </div>
      </el-col>
    </el-row>
    <el-row class="row_top row_bottom">
      <div class="table-list">
        <el-table v-loading="loading" :data="dataList.data" style="width: 100%" @sort-change="sortChange">
          <el-table-column label="项目编号" prop="date" sortable="custom" width="100"></el-table-column>
          <el-table-column label="项目名称" prop="string"></el-table-column>
          <el-table-column label="投资日期" prop="integer"></el-table-column>
          <el-table-column label="是否复投" prop="integer"></el-table-column>
          <el-table-column label="提交手机号" prop="qq_number" width="100"></el-table-column>
          <el-table-column label="投资金额" prop="float"></el-table-column>
          <el-table-column label="投资标期" prop="integer"></el-table-column>
          <el-table-column label="预估消耗" prop="integer"></el-table-column>
          <el-table-column label="投资来源" prop="integer"></el-table-column>
          <el-table-column label="返现金额" prop="integer"></el-table-column>
          <el-table-column label="审核状态" prop="integer"></el-table-column>
          <el-table-column label="审核时间" prop="integer"></el-table-column>
          <el-table-column label="备注" prop="integer"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <div class="operation_button">
                <div class="op_button_padding"><el-button size="mini" type="danger" @click="toExamine(scope.row)">审核</el-button></div>
                <div class="op_button_padding"><el-button size="mini" type="warning" @click="toExamine(scope.$index, scope.row)">删除</el-button></div>
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
        title="审核数据"
        :visible.sync="dialogVisible"
        width="35%"
        >
        <div class="form_table">
          <el-form :model="examineReason" :rules="rules" ref="examineReason" label-width="120px" class="demo-ruleForm">
            <el-form-item label="项目来源" prop="resource">
              <el-radio-group v-model="examineReason.resource">
                <el-radio label="网站"></el-radio>
                <el-radio label="渠道"></el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item label="返现金额" prop="num">
              <el-input v-model="examineReason.num"></el-input>
            </el-form-item>
            <el-form-item label="电话号码">
              <el-input v-model="examineReason.sname"></el-input>
            </el-form-item>
          </el-form>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
        </span>
      </el-dialog>
      <el-dialog
        title="正常数据导入结果"
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
    </el-row>
  </div>
</template>

<script>
import {getDaAdList} from '@/api/api'
export default {
  data () {
    return {
      inputdate0: '',
      inputdate1: '',
      inputdate2: '',
      inputdate3: '',
      projectnum: '',
      projectname: '',
      uploadURL1: 'http://mgm.fuliunion.com/Project/projectinvestdata/import_projectdata_excel/',
      uploadURL3: '',
      uploadURL4: 'http://mgm.fuliunion.com/Project/projectinvestdata/import_audit_projectdata_excel_except',
      uploadName: 'file',
      subphone: '',
      investvalue: '0',
      inmodevalue: '0',
      examinestate: '0',
      dataAdminDetails: {},
      dataList: [],
      loading: true,
      dialogVisible: false,
      uploadVisible: false,
      currentPage: 1,
      examineReason: {
        resource: '',
        num: ''
      },
      rules: {
        resource: [
          { required: true, message: '请选择项目来源', trigger: 'blur' }
        ],
        num: [
          { required: true, message: '请输入返现金额', trigger: 'blur' }
        ]
      },
      investment: [
        {
          value: '0',
          label: '全部'
        },
        {
          value: '1',
          label: '网站'
        },
        {
          value: '2',
          label: '渠道'
        }
      ],
      inmodeop: [
        {
          value: '0',
          label: '全部'
        },
        {
          value: '1',
          label: '首投'
        },
        {
          value: '2',
          label: '复投'
        }
      ],
      examine: [
        {
          value: '0',
          label: '全部'
        },
        {
          value: '1',
          label: '已审核'
        },
        {
          value: '2',
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
      getDaAdList(this.currentPage).then((res) => {
        console.log(res)
        this.loading = false
      }).catch((err) => {
        console.log(err)
      })
    },
    handleCurrentChange (val) {
      this.datalist = []
      this.loading = true
      this.currentPage = val
      this.getDatalist()
    },
    /* 正常数据导入回调 */
    handleAvatarSuccess (response, file) {
      console.log(response)
      this.uploadVisible = true
      this.dataAdminDetails = response
      this.$message('上传成功...')
    },
    /* 审核数据导入回调 */
    handleThreeSuccess () {},
    /* 异常数据导入回调 */
    handleFourSuccess () {},
    /* 数据导入前 */
    beforeAvatarUpload () {
      this.$message('正在上传...')
    },
    toExamine (row) {
      this.dialogVisible = true
    },
    sortChange (val) {
      console.log(val)
    },
    tableSelectionChange (val) {
      console.log(val)
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
      width: 120px;
      .el-input__prefix
        display: none;
    .el-input--prefix .el-input__inner
      padding-left: 10px
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
      line-height: 28px;
      width: 440px;
</style>
