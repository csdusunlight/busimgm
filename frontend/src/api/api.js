import axios from 'axios'
import qs from 'qs'
axios.defaults.withCredentials = true

let base = ''
let pageSize = 10
let http = 'http://mgm.fuliunion.com'
/* let http = 'http://127.0.0.1:8000' */

export const requestData = params => { return axios.get(`${base}/data/list/`, { params: params }) }
export const dataPage = params => { return axios.get(`${base}/data/listPage/`, { params: params }) }

/* 获取商品列表 */
export function dataPage2 (page, search) {
  let url = `${base}/data/listPage/?page=${page}&pageSize=${pageSize}`
  return axios.get(url, search)
}

/* 登录 */
export function login (data) {
  let url = `${http}/login/`
  console.log(url)
  return axios.post(url, qs.stringify(data))
}
/* 退出 */
export function logout () {
  let url = `${http}/logout/`
  console.log(url)
  return axios.post(url)
}
/* 判断是否登入 */
export function checkLogin () {
  let url = `${http}/check_user_login/`
  console.log(url)
  return axios.post(url)
}
/* ----------------项目申请审核API--------------- */
/* 获取项目审核列表 */
export function getProjectList (page, data) {
  let url = `${http}/Project/projects/?page=${page}&pageSize=${pageSize}`
  console.log(url)
  return axios.get(url, data)
}
/* 新建项目提交 */
export function postNewProject (data) {
  let url = `${http}/Project/projects/`
  return axios.post(url, data)
}
/* 获取项目数据详情 */
export function getprojectDetails (page, data) {
  let url = `${http}/statis/project_day/?page=${page}&pageSize=${pageSize}`
  console.log(url)
  return axios.get(url, data)
}
/* 修改项目 */
export function putProject (id, data) {
  let url = `${http}/Project/projects/${id}/is_altered/`
  console.log(url)
  return axios.put(url, data)
}
/* 删除项目 */
export function deleteProject (id) {
  let url = `${http}/Project/projects/${id}/`
  console.log(url)
  return axios.delete(url)
}
/* 立项项目审核 */
export function addProjectConfirm (id) {
  let url = `${http}/Project/projects/${id}/lanchedpro_approved/`
  console.log(url)
  return axios.post(url)
}
/* 立项项目拒绝 */
export function addProjectRefuse (id, data) {
  let url = `${http}/Project/projects/${id}/lanchedpro_rejected/`
  console.log(url)
  return axios.post(url, data)
}
/* 结项项目申请 */
export function endProjectApply (id, data) {
  let url = `${http}/Project/projects/${id}/concludedpro_apply/`
  console.log(url)
  return axios.post(url, data)
}
/* 结项项目审核 */
export function endProjectConfirm (id) {
  let url = `${http}/Project/projects/${id}/concludedpro_approved/`
  console.log(url)
  return axios.post(url)
}
/* 结项项目拒绝 */
export function endProjectRefuse (id, data) {
  let url = `${http}/Project/projects/${id}/concludedpro_rejected/`
  console.log(url)
  return axios.post(url, data)
}
/* ----------------费用申请审核API--------------- */
/* 获取费用申请列表 */
export function getCostList (page, data) {
  let url = `${http}/Project/fundapplys/?page=${page}&pageSize=${pageSize}`
  console.log(url)
  return axios.get(url, data)
}
/* 新建费用申请 */
export function postCost (data) {
  let url = `${http}/Project/fundapplys/`
  return axios.post(url, data)
}
/* 修改费用申请 */
export function putCost (id, data) {
  let url = `${http}/Project/fundapplys/${id}/is_altered/`
  console.log(url)
  return axios.put(url, data)
}
/* 删除费用申请 */
export function deleteCost (id) {
  let url = `${http}/Project/fundapplys/${id}/`
  console.log(url)
  return axios.delete(url)
}
/* 费用审核同意 */
export function agreeCost (id) {
  let url = `${http}/Project/fundapplys/${id}/apply_approved/`
  console.log(url)
  return axios.post(url)
}
/* 费用审核拒绝 */
export function refuseCost (id, data) {
  let url = `${http}/Project/fundapplys/${id}/apply_rejected/`
  console.log(url)
  return axios.post(url, data)
}
/* ----------------发票申请审核API--------------- */
/* 新建发票申请 */
export function postInvoice (data) {
  let url = `${http}/Project/invoiceapplys/`
  return axios.post(url, data)
}
/* 发票列表 */
export function getInvoice (page, data) {
  let url = `${http}/Project/invoiceapplys/?page=${page}&pageSize=${pageSize}`
  return axios.get(url, data)
}
/* 发票修改 */
export function putInvoice (id, data) {
  let url = `${http}/Project/invoiceapplys/${id}/is_altered/`
  console.log(url)
  return axios.put(url, data)
}
/* 删除发票 */
export function deleteInvoice (id) {
  let url = `${http}/Project/invoiceapplys/${id}/`
  console.log(url)
  return axios.delete(url)
}
/* 发票审核同意 */
export function agreeInvoice (id) {
  let url = `${http}/Project/invoiceapplys/${id}/apply_approved/`
  console.log(url)
  return axios.post(url)
}
/* 发票审核拒绝 */
export function refuseInvoice (id, data) {
  let url = `${http}/Project/invoiceapplys/${id}/apply_rejected/`
  console.log(url)
  return axios.post(url, data)
}
/* ----------------退款申请审核API--------------- */
/* 新建退款申请 */
export function postRefund (data) {
  let url = `${http}/Project/refundapplys/`
  return axios.post(url, data)
}
/* 获取退款申请列表 */
export function getRefundList (page, data) {
  let url = `${http}/Project/refundapplys/?page=${page}&pageSize=${pageSize}`
  console.log(url)
  return axios.get(url, data)
}
/* 退款申请修改修改 */
export function putRefund (id, data) {
  let url = `${http}/Project/refundapplys/${id}/is_altered/`
  console.log(url)
  return axios.put(url, data)
}
/* 删除退款 */
export function deleteRefund (id) {
  let url = `${http}/Project/refundapplys/${id}/`
  console.log(url)
  return axios.delete(url)
}
/* 退款审核同意 */
export function agreeRefund (id) {
  let url = `${http}/Project/refundapplys/${id}/apply_approved/`
  console.log(url)
  return axios.post(url)
}
/* 退款审核拒绝 */
export function refuseRefund (id, data) {
  let url = `${http}/Project/refundapplys/${id}/apply_rejected/`
  console.log(url)
  return axios.post(url, data)
}
/* ----------------数据管理API--------------- */
/* 获取数据管理列表 */
export function getDaAdList (page, data) {
  let url = `${http}/Project/projectinvestdata/?page=${page}&pageSize=${pageSize}`
  console.log(url)
  return axios.get(url, data)
}
/* 数据管理审核同意 */
export function agreeDataAdmin (id, data) {
  let url = `${http}/Project/projectinvestdata/${id}/import_apply_approved/`
  console.log(url)
  return axios.post(url, data)
}
/* 数据管理审核删除 */
export function deleteDataAdmin (id) {
  let url = `${http}/Project/projectinvestdata/${id}/`
  console.log(url)
  return axios.delete(url)
}
/* ----------------其它API--------------- */
/* 获取项目列表（其它接口获取项目名称用） */
export function allGetProject () {
  let data = {
    params: {
      state: '1'
    }
  }
  let url = `${http}/Project/projects/?page=1&pageSize=999`
  console.log(url)
  return axios.get(url, data)
}
/* 获取图片token值 */
export function getToken () {
  let url = `${http}/get_upload_token/`
  console.log(url)
  return axios.get(url)
}
/* ----------------数据总览--------------- */
export function getDataOverview () {
  let url = `${http}/statis/all/`
  console.log(url)
  return axios.get(url)
}
/* ----------------项目总览--------------- */
export function getProjectOver (page) {
  let url = `${http}/statis/day/?page=${page}&pageSize=${pageSize}`
  console.log(url)
  return axios.get(url)
}
/* ----------------项目实况列表--------------- */
export function getProjectLive (page, data) {
  let url = `${http}/Project/projects/?page=${page}&pageSize=${pageSize}`
  console.log(url)
  return axios.get(url, data)
}
