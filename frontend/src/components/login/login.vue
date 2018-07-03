<template>
  <div class="login">
    <div class="login_box"></div>
    <transition name="form-fade" mode="in-out">
      <div class="login_form">
        <div class="title">登录</div>
        <el-form :model="loginForm" :rules="rules" ref="loginForm">
          <el-form-item prop="username">
            <el-input v-model="loginForm.username" placeholder="用户名"><span>dsfsf</span></el-input>
          </el-form-item>
          <el-form-item prop="password" class="bottom">
            <el-input type="password" placeholder="密码" v-model="loginForm.password" @keyup.enter.native="submitForm('loginForm')"></el-input>
          </el-form-item>
          <div class="dl">
            <div class="cookie">
              <el-checkbox v-model="checked" style="color:#a0a0a0;">一周内自动登录</el-checkbox>
            </div>
          </div>
          <div class="botton">
            <el-button type="primary" size="mini" @click="submitForm('loginForm')" class="submit_btn">登录</el-button>
          </div>
        </el-form>
      </div>
    </transition>
  </div>
</template>

<script>
import {login} from '@/api/api'
import {mapActions} from 'vuex'
export default {
  data () {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      rules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
      },
      checked: true
    }
  },
  created () {
    this.getCookie()
  },
  methods: {
    submitForm (form) {
      var name = this.loginForm.username
      var pass = this.loginForm.password
      if (this.checked === true) {
        this.setCookie(name, pass, 7)
      }
      let para = {
        uid: name,
        upwd: pass
      }
      login(para).then((res) => {
        console.log(res)
        if (res.data.code === 0) {
          this.addName(this.loginForm.username)
          this.$router.push('/routerAdmin')
          this.$message({
            showClose: true,
            message: '恭喜您登入成功',
            type: 'success'
          })
        } else {
          console.log(res)
          this.$message(res.data.detail)
        }
      })
    },
    setCookie (name, pwd, exdays) {
      var exdate = new Date()
      exdate.setTime(exdate.getTime() + 24 * 60 * 60 * 1000 * exdays)
      window.document.cookie = 'userName' + '=' + name + ';path=/;expires=' + exdate.toGMTString()
      window.document.cookie = 'userPwd' + '=' + pwd + ';path=/;expires=' + exdate.toGMTString()
    },
    getCookie () {
      if (document.cookie.length > 0) {
        var arr = document.cookie.split('; ')
        for (var i = 0; i < arr.length; i++) {
          var arr2 = arr[i].split('=')
          if (arr2[0] === 'userName') {
            this.loginForm.username = arr2[1]
          } else if (arr2[0] === 'userPwd') {
            this.loginForm.password = arr2[1]
          }
        }
      } else {
        this.$message('账号密码已过期')
      }
    },
    clearCookie () {
      this.setCookie('', '', -1)
    },
    ...mapActions({
      addName: 'addUserName'
    })
  }
}
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .login
    width: 100%;
    height: 100%;
    background-color: #25405d;
    position: relative;
    .login_form
      position: absolute;
      width:240px;
      height: 260px;
      padding: 0 30px;
      top: 50%;
      left: 50%;
      margin-top: -180px;
      margin-left: -150px;
      overflow: hidden;
      background-color: #e0e0e2;
      .bottom
        margin-bottom: 10px;
      .title
        text-align: center;
        line-height: 55px;
        font-weight: bold;
      .el-input__inner
        border-radius: 0;
      .el-button--mini, .el-button--mini.is-round
        padding: 8px 35px;
        background-color: #000000;
        border: 0;
      .el-form-item__content
        display: flex;
        justify-content: center;
      .dl
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 12px;
        .cookie
          display: flex;
          align-items: center;
          span
            padding-left: 5px;
            cursor: pointer;
      .botton
        display: flex;
        justify-content: center;
        margin-top: 20px;
    .login_box
      width: 100%;
      height:100%;
      background: url(http://img.fuliunion.com/daniu_bg.jpg) no-repeat;
      margin: 0 auto;
      background-size: 100% 100%;
    .form-fade-enter-active, .form-fade-leave-active
      transition: all 1s;
    .form-fade-enter, .form-fade-leave-active
      transform: translate3d(0, -50px, 0);
      opacity: 0;
</style>
