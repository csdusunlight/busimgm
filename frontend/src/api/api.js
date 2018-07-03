import axios from 'axios'
import qs from 'qs'

let base = ''
let pageSize = 10
let URL = 'http://120.79.187.115'
let http = 'http://mgm.fuliunion.com'
let config = {
  withCredentials: true
}

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

/* 获取项目审核列表 */
export function getProjectList (page) {
  let url = `${http}/Project/projects/?page=${page}&pageSize=${pageSize}`
  console.log(url)
  return axios.get(url)
}
/* 新建项目提交 */
export function postNewProject (data) {
  let url = `${http}/Project/projects/`
  return axios.post(url, data)
}
/* 获取项目详情 */
export function getprojectDetails (page, project) {
  let url = `${http}/Project/projects/?page=${page}&pageSize=${pageSize}&name=${project}`
  console.log(url)
  return axios.get(url)
}
/* 获取图片token值 */
export function getToken () {
  let url = `${URL}/get_upload_token/`
  console.log(url)
  return axios.get(url)
}
