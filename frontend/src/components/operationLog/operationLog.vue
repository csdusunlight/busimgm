<template>
  <div class="operationLog">
    <el-row class="row_bottom">
      <h1 class="title">操作日志</h1>
      <div class="table-list">
        <el-table v-loading="loadingproject" :data="dataList.results" style="width: 100%">
          <el-table-column label="编号" prop="id"></el-table-column>
          <el-table-column label="操作时间" prop="otime"></el-table-column>
          <el-table-column label="操作内容" prop="oobj"></el-table-column>
          <el-table-column label="操作类型">
            <template slot-scope="scope">
              <span>{{otypeFilter[scope.row.otype]}}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作人" prop="oman"></el-table-column>
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
    </el-row>
  </div>
</template>

<script>
import {getOperationLog} from '@/api/api'
export default {
  data () {
    return {
      dataList: {},
      currentPage: 1,
      otypeFilter: {'0': '删除', '1': '修改', '2': '导入'}
    }
  },
  created () {
    this.getOperationLogList()
  },
  methods: {
    getOperationLogList () {
      getOperationLog(this.currentPage).then((res) => {
        console.log(res)
        this.dataList = res.data
      }).catch((err) => {
        console.log(err)
      })
    },
    /* 分页 */
    handleCurrentChange (val) {
      this.dataList = []
      this.loading = true
      this.currentPage = val
      this.getOperationLogList()
    }
  }
}
</script>

<style>
</style>
