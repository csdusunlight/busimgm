webpackJsonp([15],{DGHO:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var i=a("3lel"),l=a("P9l9"),s={data:function(){return{inputdate0:"",inputdate1:"",inputdate2:"",inputdate3:"",inputdate4:"",inputdate5:"",projectname:"",contractCop:"",onwcopte:"",toTakeOver:"",auditor:"",selectvalue:"0",invoicetype:"",examinestate:"0",examineData:!0,examineAdopt:!0,options:i.b,operationShow:!0,currentPage:1,dataList:[],invoicetypeop:[{value:"",label:"全部"},{value:"0",label:"专票"},{value:"1",label:"普票"}],invoiceFilter:{0:"专票",1:"普票"},loading:!0,dialogVisible:!1,modifyinvoice:{reason:""},initModifyinvoice:{reason:""},rules:{reason:[{required:!0,message:"请输入拒绝原因",trigger:"blur"}]}}},created:function(){this.getDatalist()},methods:{getDatalist:function(){var e=this,t=this.conditionDate();"0"===this.selectvalue?(this.operationShow=!0,this.examineData=!1):(this.operationShow=!1,this.examineData=!0),"2"===this.selectvalue?this.examineAdopt=!0:this.examineAdopt=!1,Object(l.A)(this.currentPage,t).then(function(t){e.dataList=t.data,e.loading=!1}).catch(function(e){console.log(e)})},conditionDate:function(){return{params:{apply_date_0:this.inputdate0,apply_date_1:this.inputdate1,audit_date_0:this.inputdate2,audit_date_1:this.inputdate3,invoice_date_0:this.inputdate4,invoice_date_1:this.inputdate5,projectname:this.projectname,contract_company:this.contractCop,company:this.onwcopte,apply_man:this.toTakeOver,audit_man:this.auditor,invoice_type:this.invoicetype,state:this.selectvalue}}},handleCurrentChange:function(e){this.dataList=[],this.loading=!0,this.currentPage=e,this.getDatalist()},sortChange:function(e){console.log(e)},invoiceAgree:function(e){var t=this;this.$confirm("请确认是否审核通过该条数据？","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){Object(l.f)(e.id).then(function(e){0===e.data.code?(t.$message({type:"success",message:"操作成功!"}),t.getDatalist()):t.$message({type:"error",message:e.detail})})}).catch(function(){console.log("cancel")})},invoiceRefuse:function(e){this.refuseId=e.id,this.dialogVisible=!0},subRefuseRefuse:function(e){var t=this;this.$refs[e].validate(function(a){if(!a)return t.$message.error("提交有误，请检查提交项！"),!1;Object(l.V)(t.refuseId,t.modifyinvoice).then(function(a){0===a.data.code?(t.modifyinvoice=t.initModifyinvoice,t.$refs[e].resetFields(),t.$message({type:"success",message:"操作成功"}),t.loading=!0,t.dialogVisible=!1,t.getDatalist()):(t.dialogVisible=!1,t.$message(a.data.detail))}).catch(function(e){console.log(e)})})},searchBtn:function(){this.currentPage=1,this.getDatalist()}},watch:{selectvalue:function(){this.datalist=[],this.currentPage=1,this.getDatalist()},invoicetype:function(){this.datalist=[],this.currentPage=1,this.getDatalist()}}},n={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"invoiceExamine"},[a("el-row",[a("el-col",{attrs:{span:24}},[a("div",{staticClass:"input_search"},[a("div",{staticClass:"search marginvi"},[a("label",{staticClass:"labeltext"},[e._v("申请日期")]),e._v(" "),a("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate0,callback:function(t){e.inputdate0=t},expression:"inputdate0"}}),e._v(" "),a("span",{staticClass:"line"},[e._v(" — ")]),e._v(" "),a("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate1,callback:function(t){e.inputdate1=t},expression:"inputdate1"}})],1),e._v(" "),a("div",{staticClass:"search"},[a("label",{staticClass:"labeltext"},[e._v("审核日期")]),e._v(" "),a("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate2,callback:function(t){e.inputdate2=t},expression:"inputdate2"}}),e._v(" "),a("span",{staticClass:"line"},[e._v(" — ")]),e._v(" "),a("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate3,callback:function(t){e.inputdate3=t},expression:"inputdate3"}})],1),e._v(" "),a("div",{staticClass:"search"},[a("label",{staticClass:"labeltext"},[e._v("开票日期")]),e._v(" "),a("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate4,callback:function(t){e.inputdate4=t},expression:"inputdate4"}}),e._v(" "),a("span",{staticClass:"line"},[e._v(" — ")]),e._v(" "),a("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate5,callback:function(t){e.inputdate5=t},expression:"inputdate5"}})],1)])])],1),e._v(" "),a("el-row",{staticClass:"row_top"},[a("el-col",{attrs:{span:24}},[a("div",{staticClass:"input_search"},[a("div",{staticClass:"search marginvi"},[a("label",{staticClass:"labeltext"},[e._v("项目名称")]),e._v(" "),a("el-input",{attrs:{size:"medium"},model:{value:e.projectname,callback:function(t){e.projectname=t},expression:"projectname"}})],1),e._v(" "),a("div",{staticClass:"search"},[a("label",{staticClass:"labeltext"},[e._v("甲方公司名称")]),e._v(" "),a("el-input",{attrs:{size:"medium"},model:{value:e.onwcopte,callback:function(t){e.onwcopte=t},expression:"onwcopte"}})],1),e._v(" "),a("div",{staticClass:"search"},[a("label",{staticClass:"labeltext"},[e._v("商务对接人")]),e._v(" "),a("el-input",{attrs:{size:"medium"},model:{value:e.toTakeOver,callback:function(t){e.toTakeOver=t},expression:"toTakeOver"}})],1),e._v(" "),a("div",{staticClass:"search"},[a("label",{staticClass:"labeltext"},[e._v("审核人")]),e._v(" "),a("el-input",{attrs:{size:"medium"},model:{value:e.auditor,callback:function(t){e.auditor=t},expression:"auditor"}})],1)])])],1),e._v(" "),a("el-row",{staticClass:"row_top"},[a("el-col",{attrs:{span:20}},[a("div",{staticClass:"flex_default"},[a("div",{staticClass:"search marginvi"},[a("label",{staticClass:"labeltext"},[e._v("签约公司")]),e._v(" "),a("el-input",{attrs:{size:"medium"},model:{value:e.contractCop,callback:function(t){e.contractCop=t},expression:"contractCop"}})],1),e._v(" "),a("div",{staticClass:"select"},[a("label",{staticClass:"label"},[e._v("发票类型")]),e._v(" "),a("el-select",{attrs:{size:"medium",placeholder:"请选择"},model:{value:e.invoicetype,callback:function(t){e.invoicetype=t},expression:"invoicetype"}},e._l(e.invoicetypeop,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}))],1),e._v(" "),a("div",{staticClass:"select"},[a("label",{staticClass:"label"},[e._v("审核状态")]),e._v(" "),a("el-select",{attrs:{size:"medium",placeholder:"请选择"},model:{value:e.selectvalue,callback:function(t){e.selectvalue=t},expression:"selectvalue"}},e._l(e.options,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}))],1)])]),e._v(" "),a("el-col",{attrs:{span:4}},[a("div",{staticClass:"flexright"},[a("el-button",{attrs:{size:"medium",type:"primary"},on:{click:e.searchBtn}},[e._v("搜索")])],1)])],1),e._v(" "),a("el-row",{staticClass:"row_top row_bottom"},[a("div",{staticClass:"table-list"},[a("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.loading,expression:"loading"}],staticStyle:{width:"100%"},attrs:{data:e.dataList.results}},[a("el-table-column",{attrs:{label:"日期",prop:"apply_date"}}),e._v(" "),a("el-table-column",{attrs:{label:"项目名称",prop:"projectname"}}),e._v(" "),a("el-table-column",{attrs:{label:"开票日期",prop:"invoice_date"}}),e._v(" "),a("el-table-column",{attrs:{label:"发票类型"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("span",[e._v(e._s(e.invoiceFilter[t.row.invoice_type]))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"签约公司",prop:"contract_company"}}),e._v(" "),a("el-table-column",{attrs:{label:"甲方公司名称",prop:"company"}}),e._v(" "),a("el-table-column",{attrs:{label:"纳税人识别号",prop:"putaxmanid"}}),e._v(" "),a("el-table-column",{attrs:{label:"开户行/银行账号"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("span",[e._v(e._s(t.row.bank)+" "+e._s(t.row.bank_account))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"注册地址/电话"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("span",[e._v(e._s(t.row.regaddress)+" "+e._s(t.row.mobile))])]}}])}),e._v(" "),a("el-table-column",{attrs:{label:"开票金额",prop:"invoice_num"}}),e._v(" "),a("el-table-column",{attrs:{label:"商务对接人",prop:"apply_man"}}),e._v(" "),e.examineData?a("el-table-column",{key:Math.random(),attrs:{label:"审核人",prop:"audit_man"}}):e._e(),e._v(" "),e.examineData?a("el-table-column",{key:Math.random(),attrs:{label:"审核时间",prop:"audit_date"}}):e._e(),e._v(" "),e.examineAdopt?a("el-table-column",{key:Math.random(),attrs:{label:"拒绝原因",prop:"audit_refused_reason"}}):e._e(),e._v(" "),a("el-table-column",{attrs:{label:"备注",prop:"record"}}),e._v(" "),e.operationShow?a("el-table-column",{key:Math.random(),attrs:{label:"操作"},scopedSlots:e._u([{key:"default",fn:function(t){return[a("div",{staticClass:"operation_button"},[a("div",{staticClass:"op_button_padding"},[a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(a){e.invoiceAgree(t.row)}}},[e._v("同意")])],1),e._v(" "),a("div",{staticClass:"op_button_padding"},[a("el-button",{attrs:{size:"mini",type:"warning"},on:{click:function(a){e.invoiceRefuse(t.row)}}},[e._v("拒绝")])],1)])]}}])}):e._e()],1)],1),e._v(" "),a("div",{staticClass:"pagination"},[a("el-pagination",{attrs:{background:"","page-size":10,"current-page":this.currentPage,layout:"prev, pager, next, total, jumper",total:this.dataList.recordCount},on:{"current-change":e.handleCurrentChange}})],1),e._v(" "),a("el-dialog",{attrs:{title:"拒绝原因",visible:e.dialogVisible,width:"35%"},on:{"update:visible":function(t){e.dialogVisible=t}}},[a("div",{staticClass:"form_table"},[a("el-form",{ref:"modifyinvoice",staticClass:"demo-ruleForm",attrs:{model:e.modifyinvoice,rules:e.rules,"label-width":"120px"}},[a("el-form-item",{attrs:{label:"拒绝原因",prop:"reason"}},[a("el-input",{attrs:{type:"textarea",size:"medium"},model:{value:e.modifyinvoice.reason,callback:function(t){e.$set(e.modifyinvoice,"reason",t)},expression:"modifyinvoice.reason"}})],1)],1)],1),e._v(" "),a("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.dialogVisible=!1}}},[e._v("取 消")]),e._v(" "),a("el-button",{attrs:{type:"primary"},on:{click:function(t){e.subRefuseRefuse("modifyinvoice")}}},[e._v("确 定")])],1)])],1)],1)},staticRenderFns:[]};var o=a("VU/8")(s,n,!1,function(e){a("wPB+")},null,null);t.default=o.exports},"wPB+":function(e,t){}});
//# sourceMappingURL=15.af0fc5c7d57c1390fd85.js.map