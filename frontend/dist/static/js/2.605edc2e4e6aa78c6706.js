webpackJsonp([2],{"3u2t":function(t,e){},ATxR:function(t,e){},kMig:function(t,e,s){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var i=s("Dd8w"),n=s.n(i),a=s("NYxO"),o=s("P9l9"),l={data:function(){return{userip:"16574146663"}},methods:{loginOut:function(){var t=this;Object(o.A)().then(function(e){0===e.data.code?(t.$message({type:"success",message:"退出成功!"}),t.$router.push("/login")):t.$message({type:"warning",message:"退出失败!"})}).catch(function(t){console.log(t)})}},computed:n()({},Object(a.c)(["username"]))},c={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"header"},[s("h1",[t._v("综合管理系统")]),t._v(" "),s("div",{staticClass:"userinfo"},[s("el-dropdown",[s("span",{staticClass:"el-dropdown-link"},[s("i",{staticClass:"iconfont"},[t._v("")])]),t._v(" "),s("el-dropdown-menu",{attrs:{slot:"dropdown"},slot:"dropdown"},[s("el-dropdown-item",[s("span",{on:{click:t.loginOut}},[t._v("退出")])])],1)],1),t._v(" "),s("p",{staticClass:"user_id"},[t._v(t._s(this.username))])],1)])},staticRenderFns:[]};var r=s("VU/8")(l,c,!1,function(t){s("ATxR")},"data-v-bc9bce8e",null).exports,v={data:function(){return{username:""}},computed:{defaultActive:function(){return this.$route.path}},created:function(){this.checkUserLogin()},methods:n()({checkUserLogin:function(){var t=this;Object(o.h)().then(function(e){if(console.log(e),1===e.data.islogin)return t.addName(e.data.mobile),!1;t.$message("您未登入过!"),t.$router.push("/login")})}},Object(a.b)({addName:"addUserName"})),components:{"v-header":r},watch:{$route:function(t,e){"/login"===t.path&&location.reload()}}},u={render:function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"routeradmin"},[s("el-row",{staticStyle:{height:"100%"}},[s("el-col",{staticStyle:{"min-height":"100%",position:"fixed","background-color":"#2b2b3a"},attrs:{span:3}},[s("div",{staticClass:"nav"},[s("el-menu",{staticClass:"el-menu-vertical-demo",attrs:{router:"","default-active":t.defaultActive,"background-color":"#2b2b3a","text-color":"#fff","active-text-color":"#ffd04b"}},[s("el-menu-item",{attrs:{index:"/projectOverview"}},[s("i",{staticClass:"iconfont iconchange iconsize"},[t._v("")]),t._v(" "),s("span",{staticClass:"iconsizetext",attrs:{slot:"title"},slot:"title"},[t._v("项目总览")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/projectLive"}},[s("i",{staticClass:"iconfont iconchange iconsize"},[t._v("")]),t._v(" "),s("span",{staticClass:"iconsizetext",attrs:{slot:"title"},slot:"title"},[t._v("项目实况")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/dataAdmin"}},[s("i",{staticClass:"iconfont iconchange"},[t._v("")]),t._v(" "),s("span",{attrs:{slot:"title"},slot:"title"},[t._v("数据管理")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/dataOverview"}},[s("i",{staticClass:"iconfont iconchange"},[t._v("")]),t._v(" "),s("span",{attrs:{slot:"title"},slot:"title"},[t._v("数据总览")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/projectApply"}},[s("i",{staticClass:"iconfont iconchange"},[t._v("")]),t._v(" "),s("span",{attrs:{slot:"title"},slot:"title"},[t._v("项目申请")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/projectExamine"}},[s("i",{staticClass:"iconfont iconchange"},[t._v("")]),t._v(" "),s("span",{attrs:{slot:"title"},slot:"title"},[t._v("项目审核")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/costApply"}},[s("i",{staticClass:"iconfont iconchange"},[t._v("")]),t._v(" "),s("span",{attrs:{slot:"title"},slot:"title"},[t._v("费用申请")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/costExamine"}},[s("i",{staticClass:"iconfont iconchange"},[t._v("")]),t._v(" "),s("span",{attrs:{slot:"title"},slot:"title"},[t._v("费用审核")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/invoiceApply"}},[s("i",{staticClass:"iconfont iconchange"},[t._v("")]),t._v(" "),s("span",{attrs:{slot:"title"},slot:"title"},[t._v("发票申请")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/invoiceExamine"}},[s("i",{staticClass:"iconfont iconchange"},[t._v("")]),t._v(" "),s("span",{attrs:{slot:"title"},slot:"title"},[t._v("发票审核")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/refundApply"}},[s("i",{staticClass:"iconfont iconchange"},[t._v("")]),t._v(" "),s("span",{attrs:{slot:"title"},slot:"title"},[t._v("退款申请")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/refundExamine"}},[s("i",{staticClass:"iconfont iconchange"},[t._v("")]),t._v(" "),s("span",{attrs:{slot:"title"},slot:"title"},[t._v("退款审核")])]),t._v(" "),s("el-menu-item",{attrs:{index:"/operationLog"}},[s("i",{staticClass:"iconfont iconchange iconsize"},[t._v("")]),t._v(" "),s("span",{staticClass:"iconsizetext",attrs:{slot:"title"},slot:"title"},[t._v("操作日志")])]),t._v(" "),s("el-menu-item",{directives:[{name:"show",rawName:"v-show",value:!1,expression:"false"}],attrs:{index:"/test"}},[s("i",{staticClass:"iconfont iconchange"},[t._v("")]),t._v(" "),s("span",{attrs:{slot:"title"},slot:"title"},[t._v("test")])])],1)],1)]),t._v(" "),s("el-col",{staticStyle:{"overflow-y":"auto",position:"absolute",top:"0",bottom:"0"},attrs:{span:21,offset:3}},[s("v-header"),t._v(" "),s("div",{staticClass:"bg-color"},[s("router-view")],1)],1)],1)],1)},staticRenderFns:[]};var d=s("VU/8")(v,u,!1,function(t){s("3u2t")},null,null);e.default=d.exports}});
//# sourceMappingURL=2.605edc2e4e6aa78c6706.js.map