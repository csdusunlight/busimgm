<template>
  <div class="header">
    <h1>聚财系统</h1>
    <div class="userinfo">
      <el-dropdown>
        <span class="el-dropdown-link">
          <i class="iconfont">&#xe60d;</i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item><span @click="loginOut">退出</span></el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <p class="user_id" >{{this.username}}</p>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import {logout} from '@/api/api'
export default {
  data () {
    return {
      userip: '16574146663'
    }
  },
  methods: {
    loginOut () {
      logout().then((res) => {
        if (res.data.code === 0) {
          this.$message({
            type: 'success',
            message: '退出成功!'
          })
          this.$router.push('/login')
        } else {
          this.$message({
            type: 'warning',
            message: '退出失败!'
          })
        }
      }).catch((err) => {
        console.log(err)
      })
    }
  },
  computed: {
    ...mapGetters([
      'username'
    ])
  }
}
</script>

<style scoped lang="stylus" rel="stylesheet/stylus">
  .header
    height: 80px;
    padding: 0 30px;
    display: flex;
    justify-content: space-between;
    h1
      font-size: 22px;
      line-height: 80px;
      font-weight: normal;
  .userinfo
    text-align: center;
    overflow: hidden;
    box-sizing: border-box;
    span
      display: inline-block;
      width:50px;
      height: 50px;
      border-radius:25px;
      line-height: 50px;
      cursor: pointer;
      background-color: #ffffff;
      i
        font-size: 36px;
        color: #333
    .user_id
      color: #333;
  .el-dropdown-menu__item
    line-height: 30px
</style>
