webpackJsonp([4],{BwnX:function(e,t){},"r/t5":function(e,t,i){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var a=i("woOf"),o=i.n(a),n=i("3lel"),l=i("P9l9"),c={data:function(){return{inputdate0:"",inputdate1:"",inputdate2:"",inputdate3:"",projectname:"",invoicetype:"",contractCop:"",nailCompany:"",examinestate:"0",options:n.b,dialogVisible:!1,invoiceVisible:!1,loading:!0,operationShow:!0,currentPage:1,dataList:[],stateFilter:n.a,invoicetypeop:[{value:"",label:"全部"},{value:"0",label:"专票"},{value:"1",label:"普票"}],invoiceFilter:{0:"专票",1:"普票"},putId:"",projectOption:[],invoice:{project:"",invoice_type:"",invoice_date:"",contract_company:"",company:"",putaxmanid:"",regaddress:"",bank_account:"",bank:"",mobile:"",invoice_num:"",record:""},rules:{project:[{required:!0,message:"选择项目",trigger:"blur"}],invoice_type:[{required:!0,message:"选择发票类型",trigger:"blur"}],invoice_date:[{required:!0,message:"选择开票时间",trigger:"blur"}],contract_company:[{required:!0,message:"请输入签约公司",trigger:"blur"}],company:[{required:!0,message:"请输入甲方公司公司",trigger:"blur"}],putaxmanid:[{required:!0,message:"请输入纳税人识别号",trigger:"blur"}],regaddress:[{required:!0,message:"请输入注册地址",trigger:"blur"}],bank_account:[{required:!0,message:"请输入银行账号",trigger:"blur"}],bank:[{required:!0,message:"请输入开户行",trigger:"blur"}],mobile:[{required:!0,message:"请输入电话",trigger:"blur"}],invoice_num:[{required:!0,message:"请输入金额",trigger:"blur"}]},modifyInvoice:{id:"",invoice_type:""}}},created:function(){this.getDatalist()},methods:{invoiceApply:function(){this.dialogVisible=!0},getDatalist:function(){var e=this,t=this.conditionDate();"0"===this.examinestate?this.operationShow=!0:this.operationShow=!1,Object(l.t)(this.currentPage,t).then(function(t){console.log(t),e.dataList=t.data,e.loading=!1}).catch(function(e){console.log(e)})},conditionDate:function(){return{params:{apply_date_0:this.inputdate0,apply_date_1:this.inputdate1,invoice_date_0:this.inputdate2,invoice_date_1:this.inputdate3,projectname:this.projectname,invoice_type:this.invoicetype,contract_company:this.contractCop,company:this.nailCompany,state:this.examinestate}}},handleCurrentChange:function(e){this.datalist=[],this.loading=!0,this.currentPage=e,this.getDatalist()},subInvoiceForm:function(e){var t=this;this.$refs[e].validate(function(i){if(!i)return t.$message.error("提交有误，请检查提交项！"),!1;Object(l.A)(t.invoice).then(function(i){0===i.data.code?(t.$refs[e].resetFields(),t.$message({type:"success",message:"发票申请成功!"}),t.dialogVisible=!1,t.getDatalist()):(t.dialogVisible=!1,t.$message(i.data.detail))}).catch(function(e){console.log(e)})})},subModifyInvoice:function(){var e=this;Object(l.E)(this.modifyInvoice.id,this.modifyInvoice).then(function(t){console.log(t),e.$message({type:"success",message:"修改成功!"}),e.invoiceVisible=!1,e.loading=!0,e.getDatalist()}).catch(function(t){e.invoiceVisible=!1,console.log(t)})},opInvoice:function(e){this.invoiceVisible=!0,o()(this.modifyInvoice,e),console.log(this.modifyInvoice)},deleteInvoiceBtn:function(e){var t=this;this.$confirm("此操作将永久删除该发票, 是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(function(){Object(l.k)(e.id).then(function(e){"0"===e.data.code?(t.$message({type:"success",message:"删除成功!"}),t.loading=!0,t.getDatalist()):t.$message(e.data.detail)})}).catch(function(){t.$message({type:"info",message:"已取消删除"})})},getProjectList:function(){var e=this;Object(l.g)().then(function(t){console.log(t.data),t.data.results.forEach(function(t,i){e.projectOption.push({value:t.id.toString(),label:t.name})}),console.log(e.projectOption)}).catch(function(e){console.log(e)})},searchBtn:function(){this.loading=!0,this.currentPage=1,this.getDatalist()}},mounted:function(){this.getProjectList()},watch:{examinestate:function(){this.dataList=[],this.loading=!0,this.currentPage=1,this.getDatalist()},invoicetype:function(){this.dataList=[],this.loading=!0,this.currentPage=1,this.getDatalist()}}},s={render:function(){var e=this,t=e.$createElement,i=e._self._c||t;return i("div",{staticClass:"invoiceadmin"},[i("el-row",[i("el-col",{attrs:{span:24}},[i("div",{staticClass:"input_search"},[i("div",{staticClass:"search marginvi search_box"},[i("label",{staticClass:"labeltext"},[e._v("申请日期")]),e._v(" "),i("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate0,callback:function(t){e.inputdate0=t},expression:"inputdate0"}}),e._v(" "),i("span",{staticClass:"line"},[e._v(" — ")]),e._v(" "),i("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate1,callback:function(t){e.inputdate1=t},expression:"inputdate1"}})],1),e._v(" "),i("div",{staticClass:"search search_box"},[i("label",{staticClass:"labeltext"},[e._v("开票日期")]),e._v(" "),i("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate2,callback:function(t){e.inputdate2=t},expression:"inputdate2"}}),e._v(" "),i("span",{staticClass:"line"},[e._v(" — ")]),e._v(" "),i("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.inputdate3,callback:function(t){e.inputdate3=t},expression:"inputdate3"}})],1),e._v(" "),i("div",{staticClass:"search"},[i("label",{staticClass:"labeltext"},[e._v("项目名称")]),e._v(" "),i("el-input",{attrs:{size:"medium"},model:{value:e.projectname,callback:function(t){e.projectname=t},expression:"projectname"}})],1),e._v(" "),i("div",{staticClass:"search"},[i("label",{staticClass:"labeltext"},[e._v("甲方公司")]),e._v(" "),i("el-input",{attrs:{size:"medium"},model:{value:e.nailCompany,callback:function(t){e.nailCompany=t},expression:"nailCompany"}})],1)])])],1),e._v(" "),i("el-row",{staticClass:"row_top"},[i("el-col",{attrs:{span:20}},[i("div",{staticClass:"flex_default"},[i("div",{staticClass:"search marginvi"},[i("label",{staticClass:"labeltext"},[e._v("签约公司")]),e._v(" "),i("el-input",{attrs:{size:"medium"},model:{value:e.contractCop,callback:function(t){e.contractCop=t},expression:"contractCop"}})],1),e._v(" "),i("div",{staticClass:"search"},[i("label",{staticClass:"labeltext"},[e._v("发票类型")]),e._v(" "),i("el-select",{attrs:{size:"medium",placeholder:"请选择"},model:{value:e.invoicetype,callback:function(t){e.invoicetype=t},expression:"invoicetype"}},e._l(e.invoicetypeop,function(e){return i("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}))],1),e._v(" "),i("div",{staticClass:"select"},[i("label",{staticClass:"label"},[e._v("审核状态")]),e._v(" "),i("el-select",{attrs:{size:"medium",placeholder:"请选择"},model:{value:e.examinestate,callback:function(t){e.examinestate=t},expression:"examinestate"}},e._l(e.options,function(e){return i("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}))],1)])]),e._v(" "),i("el-col",{attrs:{span:4}},[i("div",{staticClass:"flexright"},[i("el-button",{attrs:{size:"medium",type:"primary"},on:{click:e.searchBtn}},[e._v("搜索")])],1)])],1),e._v(" "),i("el-row",{staticClass:"row_top"},[i("el-col",{attrs:{span:4,offset:20}},[i("div",{staticClass:"flexright"},[i("el-button",{attrs:{size:"medium",type:"info"},on:{click:e.invoiceApply}},[e._v("发票申请")])],1)]),e._v(" "),i("el-dialog",{attrs:{title:"发票申请",visible:e.dialogVisible,width:"50%"},on:{"update:visible":function(t){e.dialogVisible=t}}},[i("div",{staticClass:"form_table"},[i("el-form",{ref:"invoice",staticClass:"demo-ruleForm",attrs:{model:e.invoice,rules:e.rules,"label-width":"120px"}},[i("el-form-item",{attrs:{label:"项目名称",prop:"project"}},[i("el-select",{attrs:{size:"medium",placeholder:"请选择"},model:{value:e.invoice.project,callback:function(t){e.$set(e.invoice,"project",t)},expression:"invoice.project"}},e._l(e.projectOption,function(e){return i("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}))],1),e._v(" "),i("el-form-item",{attrs:{label:"发票类型",prop:"invoice_type"}},[i("el-radio-group",{model:{value:e.invoice.invoice_type,callback:function(t){e.$set(e.invoice,"invoice_type",t)},expression:"invoice.invoice_type"}},[i("el-radio",{attrs:{label:0}},[e._v("专票")]),e._v(" "),i("el-radio",{attrs:{label:1}},[e._v("普票")])],1)],1),e._v(" "),i("el-form-item",{attrs:{label:"开票日期",prop:"invoice_date"}},[i("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.invoice.invoice_date,callback:function(t){e.$set(e.invoice,"invoice_date",t)},expression:"invoice.invoice_date"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"签约公司",prop:"contract_company"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.invoice.contract_company,callback:function(t){e.$set(e.invoice,"contract_company",t)},expression:"invoice.contract_company"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"甲方公司名称",prop:"company"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.invoice.company,callback:function(t){e.$set(e.invoice,"company",t)},expression:"invoice.company"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"纳税人识别号",prop:"putaxmanid"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.invoice.putaxmanid,callback:function(t){e.$set(e.invoice,"putaxmanid",t)},expression:"invoice.putaxmanid"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"注册地址",prop:"regaddress"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.invoice.regaddress,callback:function(t){e.$set(e.invoice,"regaddress",t)},expression:"invoice.regaddress"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"银行账号",prop:"bank_account"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.invoice.bank_account,callback:function(t){e.$set(e.invoice,"bank_account",t)},expression:"invoice.bank_account"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"开户行",prop:"bank"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.invoice.bank,callback:function(t){e.$set(e.invoice,"bank",t)},expression:"invoice.bank"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"电话",prop:"mobile"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.invoice.mobile,callback:function(t){e.$set(e.invoice,"mobile",t)},expression:"invoice.mobile"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"开票金额",prop:"invoice_num"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.invoice.invoice_num,callback:function(t){e.$set(e.invoice,"invoice_num",t)},expression:"invoice.invoice_num"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"备注",prop:"record"}},[i("el-input",{attrs:{type:"textarea",size:"medium"},model:{value:e.invoice.record,callback:function(t){e.$set(e.invoice,"record",t)},expression:"invoice.record"}})],1)],1)],1),e._v(" "),i("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{on:{click:function(t){e.dialogVisible=!1}}},[e._v("取 消")]),e._v(" "),i("el-button",{attrs:{type:"primary"},on:{click:function(t){e.subInvoiceForm("invoice")}}},[e._v("确 定")])],1)])],1),e._v(" "),i("el-row",{staticClass:"row_top row_bottom"},[i("div",{staticClass:"table-list"},[i("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.loading,expression:"loading"}],staticStyle:{width:"100%"},attrs:{data:e.dataList.results}},[i("el-table-column",{attrs:{label:"日期",prop:"apply_date",width:"100"}}),e._v(" "),i("el-table-column",{attrs:{label:"项目名称",prop:"projectname"}}),e._v(" "),i("el-table-column",{attrs:{label:"开票日期",prop:"invoice_date"}}),e._v(" "),i("el-table-column",{attrs:{label:"发票类型"},scopedSlots:e._u([{key:"default",fn:function(t){return[i("span",[e._v(e._s(e.invoiceFilter[t.row.invoice_type]))])]}}])}),e._v(" "),i("el-table-column",{attrs:{label:"签约公司",prop:"contract_company",width:"100"}}),e._v(" "),i("el-table-column",{attrs:{label:"甲方公司名称",prop:"company"}}),e._v(" "),i("el-table-column",{attrs:{label:"开票金额",prop:"invoice_num"}}),e._v(" "),i("el-table-column",{attrs:{label:"审核状态",prop:"invoice_state"},scopedSlots:e._u([{key:"default",fn:function(t){return[i("span",[e._v(e._s(e.stateFilter[t.row.state]))])]}}])}),e._v(" "),i("el-table-column",{attrs:{label:"备注",prop:"record"}}),e._v(" "),e.operationShow?i("el-table-column",{attrs:{label:"操作"},scopedSlots:e._u([{key:"default",fn:function(t){return[i("div",{staticClass:"operation_button"},[i("div",{staticClass:"op_button_padding"},[i("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(i){e.opInvoice(t.row)}}},[e._v("修改")])],1),e._v(" "),i("div",{staticClass:"op_button_padding"},[i("el-button",{attrs:{size:"mini",type:"warning"},on:{click:function(i){e.deleteInvoiceBtn(t.row)}}},[e._v("删除")])],1)])]}}])}):e._e()],1)],1),e._v(" "),i("div",{staticClass:"pagination"},[i("el-pagination",{attrs:{background:"","page-size":10,"current-page":this.currentPage,layout:"prev, pager, next, total, jumper",total:this.dataList.recordCount},on:{"current-change":e.handleCurrentChange}})],1),e._v(" "),i("el-dialog",{attrs:{title:"发票修改",visible:e.invoiceVisible,width:"50%"},on:{"update:visible":function(t){e.invoiceVisible=t}}},[i("div",{staticClass:"form_table"},[i("el-form",{ref:"modifyInvoice",staticClass:"demo-ruleForm",attrs:{model:e.modifyInvoice,rules:e.modifyInvoice,"label-width":"120px"}},[i("el-form-item",{attrs:{label:"项目名称",prop:"project"}},[i("el-select",{attrs:{size:"medium",filterable:"",placeholder:"请选择"},model:{value:e.invoice.project,callback:function(t){e.$set(e.invoice,"project",t)},expression:"invoice.project"}},e._l(e.projectOption,function(e){return i("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}))],1),e._v(" "),i("el-form-item",{attrs:{label:"发票类型",prop:"invoice_type"}},[i("el-radio",{attrs:{label:"0"},model:{value:e.modifyInvoice.invoice_type,callback:function(t){e.$set(e.modifyInvoice,"invoice_type",t)},expression:"modifyInvoice.invoice_type"}},[e._v("专票")]),e._v(" "),i("el-radio",{attrs:{label:"1"},model:{value:e.modifyInvoice.invoice_type,callback:function(t){e.$set(e.modifyInvoice,"invoice_type",t)},expression:"modifyInvoice.invoice_type"}},[e._v("普票")])],1),e._v(" "),i("el-form-item",{attrs:{label:"开票日期",prop:"invoice_date"}},[i("el-date-picker",{attrs:{format:"yyyy-MM-dd","value-format":"yyyy-MM-dd",size:"medium",type:"date",placeholder:"选择日期"},model:{value:e.modifyInvoice.invoice_date,callback:function(t){e.$set(e.modifyInvoice,"invoice_date",t)},expression:"modifyInvoice.invoice_date"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"签约公司",prop:"contract_company"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.modifyInvoice.contract_company,callback:function(t){e.$set(e.modifyInvoice,"contract_company",t)},expression:"modifyInvoice.contract_company"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"甲方公司名称",prop:"company"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.modifyInvoice.company,callback:function(t){e.$set(e.modifyInvoice,"company",t)},expression:"modifyInvoice.company"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"纳税人识别号",prop:"putaxmanid"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.modifyInvoice.putaxmanid,callback:function(t){e.$set(e.modifyInvoice,"putaxmanid",t)},expression:"modifyInvoice.putaxmanid"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"注册地址",prop:"regaddress"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.modifyInvoice.regaddress,callback:function(t){e.$set(e.modifyInvoice,"regaddress",t)},expression:"modifyInvoice.regaddress"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"银行账号",prop:"bank_account"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.modifyInvoice.bank_account,callback:function(t){e.$set(e.modifyInvoice,"bank_account",t)},expression:"modifyInvoice.bank_account"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"开户行",prop:"bank"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.modifyInvoice.bank,callback:function(t){e.$set(e.modifyInvoice,"bank",t)},expression:"modifyInvoice.bank"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"电话",prop:"mobile"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.modifyInvoice.mobile,callback:function(t){e.$set(e.modifyInvoice,"mobile",t)},expression:"modifyInvoice.mobile"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"开票金额",prop:"invoice_num"}},[i("el-input",{attrs:{size:"medium"},model:{value:e.modifyInvoice.invoice_num,callback:function(t){e.$set(e.modifyInvoice,"invoice_num",t)},expression:"modifyInvoice.invoice_num"}})],1),e._v(" "),i("el-form-item",{attrs:{label:"备注",prop:"record"}},[i("el-input",{attrs:{type:"textarea",size:"medium"},model:{value:e.modifyInvoice.record,callback:function(t){e.$set(e.modifyInvoice,"record",t)},expression:"modifyInvoice.record"}})],1)],1)],1),e._v(" "),i("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{on:{click:function(t){e.invoiceVisible=!1}}},[e._v("取 消")]),e._v(" "),i("el-button",{attrs:{type:"primary"},on:{click:e.subModifyInvoice}},[e._v("确 定")])],1)])],1)],1)},staticRenderFns:[]};var r=i("VU/8")(c,s,!1,function(e){i("BwnX")},null,null);t.default=r.exports}});
//# sourceMappingURL=4.23cf9aa6a685b61133ee.js.map