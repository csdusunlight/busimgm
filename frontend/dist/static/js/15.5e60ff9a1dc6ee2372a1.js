webpackJsonp([15],{"4Ffk":function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var i=a("P9l9"),s=a("3lel"),l={data:function(){return{inputdate0:"",inputdate1:"",inputdate2:"",inputdate3:"",projectnum:"",projectnameVal:"",uploadURL1:i.L,uploadURL3:i.s,uploadURL4:i.a,exportExcelUrl:i.t,uploadName:"file",subphone:"",investvalue:"",stateFilter:s.a,inmodevalue:"",examinestate:"",adoptId:"",dataAdminDetails:{},investFilter:{true:"是",false:"否"},sourceFilter:{site:"网站",channel:"渠道"},dataList:[],loading:!0,dialogVisible:!1,uploadVisible:!1,uploadThreeVisible:!1,currentPage:1,examineReason:{source:"",return_amount:""},initExamineReason:{source:"",return_amount:""},rules:{source:[{required:!0,message:"请选择项目来源",trigger:"blur"}],return_amount:[{required:!0,message:"请输入返现金额",trigger:"blur"}]},investment:[{value:"",label:"全部"},{value:"site",label:"网站"},{value:"channel",label:"渠道"}],inmodeop:[{value:"",label:"全部"},{value:!0,label:"复投"},{value:!1,label:"首投"}],examine:[{value:"",label:"全部"},{value:"1",label:"已审核"},{value:"0",label:"待审核"}]}},created:function(){this.getDatalist()},methods:{getDatalist:function(){var e=this,t=this.conditionDate();Object(i.w)(this.currentPage,t).then(function(t){e.dataList=t.data,console.log(e.dataList),e.loading=!1}).catch(function(e){console.log(e)})},conditionDate:function(){return""!==this.inputdate2&&""!==this.inputdate3?{params:{investtime_0:this.inputdate0,investtime_1:this.inputdate1,audittime_0:this.inputdate2+" 00:00:00",audittime_1:this.inputdate3+" 23:59:59",project:this.projectnum,invest_mobile:this.subphone,projectname:this.projectnameVal,source:this.investvalue,is_futou:this.inmodevalue,state:this.examinestate}}:{params:{investtime_0:this.inputdate0,investtime_1:this.inputdate1,project:this.projectnum,invest_mobile:this.subphone,projectname:this.projectnameVal,source:this.investvalue,is_futou:this.inmodevalue,state:this.examinestate}}},handleCurrentChange:function(e){this.loading=!0,this.datalist=[],this.currentPage=e,this.getDatalist()},exportExel:function(){console.log("数据导出");var e=this.exportExcelUrl;console.log(e);var t='<form action="'+e+'" method="get" target="_self" id="postData_form">';t+='<input name="investtime_0" type="hidden" value="'+this.inputdate0+'"/>',t+='<input name="investtime_1" type="hidden" value="'+this.inputdate1+'"/>',t+='<input name="audittime_0" type="hidden" value="'+this.inputdate2+'"/>',t+='<input name="audittime_1" type="hidden" value="'+this.inputdate3+'"/>',t+='<input name="project" type="hidden" value="'+this.projectnum+'"/>',t+='<input name="projectname" type="hidden" value="'+this.projectnameVal+'"/>',t+='<input name="invest_mobile" type="hidden" value="'+this.subphone+'"/>',t+='<input name="source" type="hidden" value="'+this.investvalue+'"/>',t+='<input name="is_futou" type="hidden" value="'+this.inmodevalue+'"/>',t+='<input name="state" type="hidden" value="'+this.examinestate+'"/>',t+="</form>";var a=document.getElementById("myIFrame");a.contentWindow.document.open(),a.contentWindow.document.write(t),a.contentWindow.document.close(),document.getElementById("myIFrame").contentWindow.document.getElementById("postData_form").submit()},handleAvatarSuccess:function(e,t){console.log(e),0===e.code?(this.$message({type:"success",message:"上传成功!"}),this.uploadVisible=!0,this.dataAdminDetails=e.data,this.getDatalist()):this.$message.error(e.detail)},handleThreeSuccess:function(e,t){console.log(e),0===e.code?(this.$message({type:"success",message:"上传成功!"}),this.$notify({title:"成功",message:"上传成功条数: "+e.data.num,type:"success"}),this.getDatalist()):this.$message.error(e.detail)},handleFourSuccess:function(e,t){console.log(e),0===e.code?(this.$message({type:"success",message:"上传成功!"}),this.$notify({title:"成功",message:"上传成功条数: "+e.data.num,type:"success"}),this.getDatalist()):this.$message.error(e.detail)},beforeAvatarUpload:function(){this.$message("正在上传...")},deleteDataAdminBtn:function(e){var t=this;this.$confirm("请确认是否删除该条数据？","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){Object(i.l)(e.id).then(function(e){console.log(e),0===e.data.code?(t.$message({type:"success",message:"操作成功!"}),t.getDatalist()):t.$message({type:"error",message:e.data.detail})})}).catch(function(){console.log("cancel")})},searchBtn:function(){this.currentPage=1,this.getDatalist()},AgreeDataAdminBtn:function(e){this.dialogVisible=!0,this.adoptId=e.id,this.examineReason.source=e.source,this.examineReason.return_amount=e.return_amount,this.examineReason.invest_mobile=e.invest_mobile},subDataAdminBtn:function(e){var t=this;this.$refs[e].validate(function(a){if(!a)return t.$message.error("提交有误，请检查提交项！"),!1;Object(i.e)(t.adoptId,t.examineReason).then(function(a){console.log(a),0===a.data.code?(t.examineReason=t.initExamineReason,t.$refs[e].resetFields(),t.$message({type:"success",message:"审核数据成功"}),t.loading=!0,t.dialogVisible=!1,t.getDatalist()):(t.dialogVisible=!1,t.$message(a.data.detail))}).catch(function(e){console.log(e)})})},tableSelectionChange:function(e){console.log(e)}},watch:{inmodevalue:function(){this.loading=!0,this.dataList=[],this.currentPage=1,this.getDatalist()},investvalue:function(){this.loading=!0,this.dataList=[],this.currentPage=1,this.getDatalist()},examinestate:function(){this.loading=!0,this.dataList=[],this.currentPage=1,this.getDatalist()}}},n={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"dataadmin"},[a("el-row",[a("el-col",{attrs:{span:24}},[a("div",{staticClass:"input_search"},[a("div",{staticClass:"search marginvi search_box"},[a("label",{staticClass:"labeltext"},[e._v("投资日期")]),e._v(" "),a("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate0,callback:function(t){e.inputdate0=t},expression:"inputdate0"}}),e._v(" "),a("span",{staticClass:"line"},[e._v(" — ")]),e._v(" "),a("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate1,callback:function(t){e.inputdate1=t},expression:"inputdate1"}})],1),e._v(" "),a("div",{staticClass:"search search_box"},[a("label",{staticClass:"labeltext"},[e._v("审核时间")]),e._v(" "),a("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate2,callback:function(t){e.inputdate2=t},expression:"inputdate2"}}),e._v(" "),a("span",{staticClass:"line"},[e._v(" — ")]),e._v(" "),a("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate3,callback:function(t){e.inputdate3=t},expression:"inputdate3"}})],1),e._v(" "),a("div",{staticClass:"search"},[a("label",{staticClass:"labeltext"},[e._v("项目编号")]),e._v(" "),a("el-input",{attrs:{size:"medium"},model:{value:e.projectnum,callback:function(t){e.projectnum=t},expression:"projectnum"}})],1),e._v(" "),a("div",{staticClass:"search"},[a("label",{staticClass:"labeltext"},[e._v("项目名称")]),e._v(" "),a("el-input",{attrs:{size:"medium"},model:{value:e.projectnameVal,callback:function(t){e.projectnameVal=t},expression:"projectnameVal"}})],1)])])],1),e._v(" "),a("el-row",[a("el-col",{attrs:{span:20}},[a("div",{staticClass:"input_search row_top"},[a("div",{staticClass:"search marginvi"},[a("label",{staticClass:"labeltext"},[e._v("提交手机号")]),e._v(" "),a("el-input",{attrs:{size:"medium"},model:{value:e.subphone,callback:function(t){e.subphone=t},expression:"subphone"}})],1),e._v(" "),a("div",{staticClass:"select margin_clear"},[a("label",{staticClass:"label"},[e._v("投资来源")]),e._v(" "),a("el-select",{attrs:{size:"medium",placeholder:"请选择"},model:{value:e.investvalue,callback:function(t){e.investvalue=t},expression:"investvalue"}},e._l(e.investment,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}))],1),e._v(" "),a("div",{staticClass:"select"},[a("label",{staticClass:"label"},[e._v("投资方式")]),e._v(" "),a("el-select",{attrs:{size:"medium",placeholder:"请选择"},model:{value:e.inmodevalue,callback:function(t){e.inmodevalue=t},expression:"inmodevalue"}},e._l(e.inmodeop,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}))],1),e._v(" "),a("div",{staticClass:"select"},[a("label",{staticClass:"label"},[e._v("审核状态")]),e._v(" "),a("el-select",{attrs:{size:"medium",placeholder:"请选择"},model:{value:e.examinestate,callback:function(t){e.examinestate=t},expression:"examinestate"}},e._l(e.examine,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}))],1)])]),e._v(" "),a("el-col",{attrs:{span:4}},[a("div",{staticClass:"flexright"},[a("el-button",{attrs:{size:"medium",type:"primary"},on:{click:e.searchBtn}},[e._v("搜索")])],1)])],1),e._v(" "),a("el-row",[a("el-col",{attrs:{span:24}},[a("div",{staticClass:"flexright"},[a("el-upload",{staticClass:"avatar-uploader",attrs:{action:e.uploadURL1,name:e.uploadName,"show-file-list":!1,"on-success":e.handleAvatarSuccess,"before-upload":e.beforeAvatarUpload}},[a("el-button",{attrs:{size:"medium",type:"info"}},[e._v("导入")])],1),e._v(" "),a("el-button",{attrs:{size:"medium",type:"info"},on:{click:e.exportExel}},[e._v("导出")]),e._v(" "),a("el-upload",{staticClass:"avatar-uploader",attrs:{action:e.uploadURL3,name:e.uploadName,"with-credentials":!0,"show-file-list":!1,"on-success":e.handleThreeSuccess,"before-upload":e.beforeAvatarUpload}},[a("el-button",{attrs:{size:"medium",type:"info"}},[e._v("审核数据导入")])],1),e._v(" "),a("el-upload",{staticClass:"avatar-uploader",attrs:{action:e.uploadURL4,name:e.uploadName,"with-credentials":!0,"show-file-list":!1,"on-success":e.handleFourSuccess,"before-upload":e.beforeAvatarUpload}},[a("el-button",{attrs:{size:"medium",type:"info"}},[e._v("异常数据导入")])],1),e._v(" "),a("a",{attrs:{href:"http://mgm.fuliunion.com/static/projectdata_init_template.xls"}},[a("el-button",{attrs:{size:"medium",type:"info"}},[e._v("获取初始导入模板")])],1)],1)])],1),e._v(" "),a("el-row",{staticClass:"row_top row_bottom"},[a("div",{staticClass:"table-list"},[a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.loading,expression:"loading"}],staticStyle:{width:"100%"},attrs:{data:e.dataList.results}},[a("el-table-column",{attrs:{label:"项目编号",prop:"project",width:"100"}}),e._v(" "),a("el-table-column",{attrs:{label:"项目名称",prop:"projectname"}}),e._v(" "),a("el-table-column",{attrs:{label:"投资日期",prop:"invest_time"}}),e._v(" "),a("el-table-column",{attrs:{label:"是否复投",prop:"is_futou"},scopedSlots:e._u([{key:"default",fn:function(t){return[t.row.is_futou?a("span",[e._v("复投")]):a("span",[e._v("首投")])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"提交手机号",prop:"invest_mobile",width:"100"}}),e._v(" "),a("el-table-column",{attrs:{label:"投资金额",prop:"invest_amount"}}),e._v(" "),a("el-table-column",{attrs:{label:"投资标期",prop:"invest_term"}}),e._v(" "),a("el-table-column",{attrs:{label:"预估消耗",prop:"settle_amount"}}),e._v(" "),a("el-table-column",{attrs:{label:"投资来源"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("span",[e._v(e._s(e.sourceFilter[t.row.source]))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"返现金额",prop:"return_amount"}}),e._v(" "),a("el-table-column",{attrs:{label:"审核状态"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("span",[e._v(e._s(e.stateFilter[t.row.state]))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"审核时间",prop:"audit_time"}}),e._v(" "),a("el-table-column",{attrs:{label:"备注",prop:"remark"}}),e._v(" "),a("el-table-column",{attrs:{label:"操作"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("div",{staticClass:"operation_minimalism"},[a("span",{staticClass:"minimalism"},[a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(a){e.AgreeDataAdminBtn(t.row)}}},[e._v("审核")])],1),e._v("\n              |\n              "),a("span",{staticClass:"minimalism"},[a("el-button",{attrs:{size:"mini",type:"warning"},on:{click:function(a){e.deleteDataAdminBtn(t.row)}}},[e._v("删除")])],1)])]}}])})],1)],1),e._v(" "),a("div",{staticClass:"pagination"},[a("el-pagination",{attrs:{background:"","page-size":10,"current-page":this.currentPage,layout:"prev, pager, next, total, jumper",total:this.dataList.recordCount},on:{"current-change":e.handleCurrentChange}})],1),e._v(" "),a("el-dialog",{attrs:{title:"审核数据",visible:e.dialogVisible,width:"35%"},on:{"update:visible":function(t){e.dialogVisible=t}}},[a("div",{staticClass:"form_table"},[a("el-form",{ref:"examineReason",staticClass:"demo-ruleForm",attrs:{model:e.examineReason,rules:e.rules,"label-width":"120px"}},[a("el-form-item",{attrs:{label:"投资来源",prop:"source"}},[a("el-radio-group",{model:{value:e.examineReason.source,callback:function(t){e.$set(e.examineReason,"source",t)},expression:"examineReason.source"}},[a("el-radio",{attrs:{label:"site"}},[e._v("网站")]),e._v(" "),a("el-radio",{attrs:{label:"channel"}},[e._v("渠道")])],1)],1),e._v(" "),a("el-form-item",{attrs:{label:"返现金额",prop:"return_amount"}},[a("el-input",{model:{value:e.examineReason.return_amount,callback:function(t){e.$set(e.examineReason,"return_amount",t)},expression:"examineReason.return_amount"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"电话号码"}},[a("el-input",{model:{value:e.examineReason.invest_mobile,callback:function(t){e.$set(e.examineReason,"invest_mobile",t)},expression:"examineReason.invest_mobile"}})],1)],1)],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.dialogVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:function(t){e.subDataAdminBtn("examineReason")}}},[e._v("确 定")])],1)]),e._v(" "),a("el-dialog",{attrs:{title:"一次数据导入结果",visible:e.uploadVisible,width:"520px"},on:{"update:visible":function(t){e.uploadVisible=t}}},[a("div",{staticClass:"information"},[a("p",[e._v("总上传数据条数："+e._s(e.dataAdminDetails.anum))]),e._v(" "),a("p",[e._v("上传成功数据条数："+e._s(e.dataAdminDetails.num))]),e._v(" "),a("p",[e._v("表格重复数据条数："+e._s(e.dataAdminDetails.dup1))]),e._v(" "),a("p",[e._v("数据库重复数据条数："+e._s(e.dataAdminDetails.dup2))]),e._v(" "),a("div",{staticClass:"text"},[e._v("重复手机号："+e._s(e.dataAdminDetails.dupstr))])])]),e._v(" "),a("el-dialog",{attrs:{title:"审核数据导入结果",visible:e.uploadThreeVisible,width:"520px"},on:{"update:visible":function(t){e.uploadThreeVisible=t}}},[a("div",{staticClass:"information"},[a("p",[e._v("上传成功数据条数："+e._s(e.dataAdminDetails.num))])])])],1),e._v(" "),a("iframe",{staticStyle:{display:"none"},attrs:{id:"myIFrame",scrolling:"yes",frameborder:"1"}})],1)},staticRenderFns:[]};var o=a("VU/8")(l,n,!1,function(e){a("laYE")},null,null);t.default=o.exports},laYE:function(e,t){}});
//# sourceMappingURL=15.5e60ff9a1dc6ee2372a1.js.map