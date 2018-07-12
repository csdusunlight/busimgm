<template>
  <div class="routeradmin">
    <el-row style="height: 100%">
      <el-col :span="3" style="min-height: 100%; position: fixed; background-color: #2b2b3a;">
        <div class="nav">
          <el-menu
            router
            :default-active="defaultActive"
            class="el-menu-vertical-demo"
            background-color="#2b2b3a"
            text-color="#fff"
            active-text-color="#ffd04b"
          >
            <el-menu-item index="/projectOverview" v-if="jurisdiction === 'SHRY' || jurisdiction === 'SJRY' || jurisdiction === 'ADMIN'">
              <i class="iconfont iconchange iconsize">&#xe607;</i>
              <span class="iconsizetext" slot="title">项目总览</span>
            </el-menu-item>
            <el-menu-item index="/projectLive" v-if="jurisdiction === 'SHRY' || jurisdiction === 'SJRY' || jurisdiction === 'ADMIN' || true">
              <i class="iconfont iconchange iconsize">&#xe6c0;</i>
              <span class="iconsizetext" slot="title">项目实况</span>
            </el-menu-item>
            <el-menu-item index="/dataAdmin" v-if="jurisdiction === 'SJRY' || jurisdiction === 'ADMIN'">
              <i class="iconfont iconchange">&#xe614;</i>
              <span slot="title">投资数据</span>
            </el-menu-item>
            <el-menu-item index="/dataOverview" v-if="jurisdiction === 'SWRY' || jurisdiction === 'ADMIN'">
              <i class="iconfont iconchange">&#xe609;</i>
              <span slot="title">个人数据</span>
            </el-menu-item>
            <el-menu-item index="/projectApply" v-if="jurisdiction === 'SWRY' || jurisdiction === 'SJRY' || jurisdiction === 'ADMIN'">
              <i class="iconfont iconchange">&#xe6c2;</i>
              <span slot="title">项目申请</span>
            </el-menu-item>
            <el-menu-item index="/projectExamine" v-if="jurisdiction === 'SHRY' || jurisdiction === 'ADMIN'">
              <i class="iconfont iconchange">&#xe6c2;</i>
              <span slot="title">项目审核</span>
            </el-menu-item>
            <el-menu-item index="/costApply" v-if="jurisdiction === 'SWRY' || jurisdiction === 'ADMIN'">
              <i class="iconfont iconchange">&#xe608;</i>
              <span slot="title">费用申请</span>
            </el-menu-item>
            <el-menu-item index="/costExamine" v-if="jurisdiction === 'SHRY' || jurisdiction === 'CWRY' || jurisdiction === 'ADMIN'">
              <i class="iconfont iconchange">&#xe608;</i>
              <span slot="title">费用审核</span>
            </el-menu-item>
            <el-menu-item index="/invoiceApply" v-if="jurisdiction === 'SWRY' || jurisdiction === 'ADMIN'">
              <i class="iconfont iconchange">&#xe654;</i>
              <span slot="title">发票申请</span>
            </el-menu-item>
            <el-menu-item index="/invoiceExamine" v-if="jurisdiction === 'SHRY' || jurisdiction === 'CWRY' || jurisdiction === 'ADMIN'">
              <i class="iconfont iconchange">&#xe654;</i>
              <span slot="title">发票审核</span>
            </el-menu-item>
            <el-menu-item index="/refundApply" v-if="jurisdiction === 'SWRY' || jurisdiction === 'ADMIN'">
              <i class="iconfont iconchange">&#xe617;</i>
              <span slot="title">退款申请</span>
            </el-menu-item>
            <el-menu-item index="/refundExamine" v-if="jurisdiction === 'SHRY' || jurisdiction === 'CWRY' || jurisdiction === 'ADMIN'">
              <i class="iconfont iconchange">&#xe617;</i>
              <span slot="title">退款审核</span>
            </el-menu-item>
            <el-menu-item index="/operationLog">
              <i class="iconfont iconchange iconsize">&#xe600;</i>
              <span class="iconsizetext" slot="title">操作日志</span>
            </el-menu-item>
            <el-menu-item index="/test" v-show="false">
              <i class="iconfont iconchange">&#xe617;</i>
              <span slot="title">test</span>
            </el-menu-item>
          </el-menu>
        </div>
      </el-col>
      <el-col :span="21" :offset="3" style="overflow-y: auto; position: absolute; top: 0; bottom: 0;">
         <v-header></v-header>
        <div class="bg-color">
          <router-view></router-view>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import header from '@/components/header/header'
import {checkLogin} from '@/api/api'
import {mapActions, mapGetters} from 'vuex'
export default {
  data () {
    return {
      username: '',
      jutionrow: {}
    }
  },
  computed: {
    defaultActive () {
      return this.$route.path
    },
    ...mapGetters([
      'jurisdiction'
    ])
  },
  created () {
    this.checkUserLogin()
  },
  methods: {
    checkUserLogin () {
      checkLogin().then((res) => {
        console.log(res)
        if (res.data.islogin === 1) {
          this.jutionrow = res.data.permission[0]
          this.addJution(this.jutionrow)
          this.addName(res.data.mobile)
          this.addUserId(res.data.userid)
          if (res.data.permission[0] === 'SWRY') {
            this.$router.push('/dataOverview')
          }
          if (res.data.permission[0] === 'CWRY') {
            this.$router.push('/costExamine')
          }
          return false
        } else {
          this.$message('您未登入过!')
          this.$router.push('/login')
        }
      })
    },
    ...mapActions({
      addName: 'addUserName',
      addUserId: 'addUserId',
      addJution: 'jurisdictionRow'
    })
  },
  components: {
    'v-header': header
  },
  watch: {
    '$route' (to, from) {
      if (to.path === '/login') {
        location.reload()
      }
    }
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .routeradmin
    height: 100%
  .iconchange
    font-size: 22px
    color: #fff
  .iconsize
    font-size: 28px
    position: relative;
    left: -3px;
    top: 0;
  .iconsizetext
    position: relative;
    left: -6px;
    top: 0;
  .nav
    margin-top: 20px;
    .el-menu-item
      padding-left: 25px !important
    .el-menu-item span
      margin-left:15px
  .bg-color
    height: 100%;
    background-color: #ffffff;
    box-sizing: border-box;
    border-top:15px solid #f5f5f5;
    padding: 20px 30px;
    padding-bottom: 80px;
</style>
