webpackJsonp([8],{AUBu:function(t,e){},rB1b:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=a("P9l9"),o={data:function(){return{dataList:{},currentPage:1,otypeFilter:{0:"删除",1:"修改",2:"导入"}}},created:function(){this.getOperationLogList()},methods:{getOperationLogList:function(){var t=this;Object(n.B)(this.currentPage).then(function(e){t.dataList=e.data}).catch(function(t){console.log(t)})},handleCurrentChange:function(t){this.dataList=[],this.loading=!0,this.currentPage=t,this.getOperationLogList()}}},r={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"operationLog"},[a("el-row",{staticClass:"row_bottom"},[a("h1",{staticClass:"title"},[t._v("操作日志")]),t._v(" "),a("div",{staticClass:"table-list"},[a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:t.loadingproject,expression:"loadingproject"}],staticStyle:{width:"100%"},attrs:{data:t.dataList.results}},[a("el-table-column",{attrs:{label:"编号",prop:"id"}}),t._v(" "),a("el-table-column",{attrs:{label:"操作人",prop:"oman"}}),t._v(" "),a("el-table-column",{attrs:{label:"操作时间",prop:"otime"}}),t._v(" "),a("el-table-column",{attrs:{label:"操作类型"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("span",[t._v(t._s(t.otypeFilter[e.row.otype]))])]}}])}),t._v(" "),a("el-table-column",{attrs:{label:"操作内容",prop:"oobj"}})],1)],1),t._v(" "),a("div",{staticClass:"pagination"},[a("el-pagination",{attrs:{background:"","page-size":10,"current-page":this.currentPage,layout:"prev, pager, next, total, jumper",total:this.dataList.recordCount},on:{"current-change":t.handleCurrentChange}})],1)])],1)},staticRenderFns:[]};var l=a("VU/8")(o,r,!1,function(t){a("AUBu")},null,null);e.default=l.exports}});
//# sourceMappingURL=8.b7be03c6c4b1b4d298a0.js.map