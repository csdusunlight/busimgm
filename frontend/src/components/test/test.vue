<template>
  <div>
    <div class="select">
      <label class="label">项目状态</label>
      <el-select size="medium" v-model="state" placeholder="请选择">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-button @click="exportExel" type="primary">导出测试</el-button>
    </div>
    <el-table
      :data="tableData"
      style="width: 100%"
      @sort-change="sortChange"
      ref="table2"
    >
      <el-table-column
        prop="date"
        label="日期">
      </el-table-column>
      <el-table-column
        :key="Math.random()"
        v-if="state === '0'"
        prop="name"
        label="姓名2">
      </el-table-column>
      <el-table-column
        :key="Math.random()"
        v-if="state === '0' || state === '1'"
        prop="name"
        label="姓名">
      </el-table-column>
      <el-table-column
        prop="integer"
        label="金额">
      </el-table-column>
      <el-table-column
        prop="integer2"
        label="标期">
      </el-table-column>
      <el-table-column
        :key="Math.random()"
        v-if="state === '2'"
        prop="remark"
        label="备注">
      </el-table-column>
    </el-table>
    <el-table
      :data="tableData"
      style="width: 100%"
      @sort-change="sortChange"
      ref="table"
      v-show="false"
    >
      <el-table-column
        v-for="{ prop, label } in colConfigs"
        :key="prop"
        :prop="prop"
        :label="label">
      </el-table-column>
    </el-table>
    <div class="pagination" style="display: flex;justify-content: flex-end;">
      <el-pagination
        background
        @current-change="handleCurrentChange"
        :page-size="pageSize"
        :current-page="currentPage"
        layout="total, prev, pager, next, jumper"
        :total="total">
      </el-pagination>
    </div>
    <iframe id="myIFrame" scrolling="yes" style="display:none" frameborder=1></iframe>
  </div>
</template>

<script>
import { requestData, dataPage } from '@/api/api'

export default {
  data () {
    return {
      colConfigs: [
        {prop: 'date', label: '日期'},
        {prop: 'name', label: '姓名'},
        {prop: 'integer', label: '金额'},
        {prop: 'integer2', label: '标期'},
        {prop: 'string', label: '备注'}
      ],
      state: '0',
      options: [
        {
          value: '0',
          label: '全部'
        },
        {
          value: '1',
          label: '正在进行'
        },
        {
          value: '2',
          label: '已结项'
        }
      ],
      tableData: [],
      currentPage: 1,
      pageSize: 10,
      total: 0
    }
  },
  watch: {
    state: function (val, oldVal) {
      console.log(val)
      if (val === '0') {
        this.colConfigs = [
          {prop: 'date', label: '日期'},
          {prop: 'name', label: '姓名'},
          {prop: 'integer', label: '金额'},
          {prop: 'integer2', label: '标期'},
          {prop: 'string', label: '备注'}
        ]
      } else if (val === '1') {
        this.colConfigs = [
          {prop: 'date', label: '日期'},
          {prop: 'name', label: '姓名'},
          {prop: 'integer', label: '金额'},
          {prop: 'string2', label: '测试'},
          {prop: 'integer2', label: '标期'},
          {prop: 'string', label: '备注'}
        ]
      } else if (val === '2') {
        this.colConfigs = [
          {prop: 'date', label: '日期'},
          {prop: 'name', label: '姓名'},
          {prop: 'integer', label: '金额'},
          {prop: 'integer2', label: '标期'},
          {prop: 'qq_number', label: '测试2'},
          {prop: 'string', label: '备注'}
        ]
      }
      console.log(this.colConfigs)
    }
  },
  methods: {
    exportExel () {
      var exportUrl = 'http://127.0.0.1:8000/Admin/export_investlog/'
      console.log('导出测试')
      var html = '<form action="' + exportUrl + '" method="get" target="_self" id="postData_form">'
      html += '<input name="audit_state" type="hidden" value="' + this.state + '"/>'
      html += '</form>'
      var iframe = document.getElementById('myIFrame')
      iframe.contentWindow.document.open()
      iframe.contentWindow.document.write(html)
      iframe.contentWindow.document.close()
      document.getElementById('myIFrame').contentWindow.document.getElementById('postData_form').submit()
    },
    handleCurrentChange (val) {
      console.log(this)
      console.log(val)
      var param = {
        page: val
      }
      this.getDataList(param)
    },
    sortChange (val) {
      console.log(val)
    },
    getDataList (param) {
      dataPage(param).then((res) => {
        if (res.status === 200) {
          console.log(res)
          this.tableData = res.data.data
          this.total = res.data.total
          console.log(this.tableData)
        } else {
          this.loading = false
          console.log('请求数据失败')
        }
      })
    }
  },
  created () {
    var param = {
      page: 1
    }
    this.getDataList(param)
    requestData().then((res) => {
      if (res.status === 200) {
        console.log(res)
      } else {
        this.loading = false
        console.log('请求数据失败')
      }
    })
  }
}
</script>

<style>
</style>
