<template>
  <div>
      <el-table
        :data="tableData"
        style="width: 100%"
        @sort-change="sortChange"
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
      state: 0,
      tableData: [],
      currentPage: 1,
      pageSize: 10,
      total: 0
    }
  },
  methods: {
    handleCurrentChange (val) {
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
