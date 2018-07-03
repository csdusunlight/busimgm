import Vue from 'vue'
import Router from 'vue-router'

const projectOverview = () => import('@/components/projectOverview/projectOverview')
const projectLive = () => import('@/components/projectLive/projectLive')
const dataAdmin = () => import('@/components/dataAdmin/dataAdmin')
const dataOverview = () => import('@/components/dataOverview/dataOverview')
const projectApply = () => import('@/components/projectApply/projectApply')
const projectExamine = () => import('@/components/projectExamine/projectExamine')
const costAdmin = () => import('@/components/costAdmin/costAdmin')
const invoiceExamine = () => import('@/components/invoiceExamine/invoiceExamine')
const invoiceApply = () => import('@/components/invoiceApply/invoiceApply')
const refundAdmin = () => import('@/components/refundAdmin/refundAdmin')
const operationLog = () => import('@/components/operationLog/operationLog')
const login = () => import('@/components/login/login')

const routerAdmin = () => import('@/components/routerAdmin/routerAdmin')
const test = () => import('@/components/test/test')

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: login
    },
    {
      path: '/login',
      component: login
    },
    {
      path: '/routerAdmin',
      component: routerAdmin,
      children: [
        {
          path: '/',
          redirect: '/projectOverview'
        },
        {
          path: '/projectOverview',
          name: 'projectOverview',
          component: projectOverview
        },
        {
          path: '/projectLive',
          name: 'projectLive',
          component: projectLive
        },
        {
          path: '/dataAdmin',
          name: 'dataAdmin',
          component: dataAdmin
        },
        {
          path: '/dataOverview',
          name: 'dataOverview',
          component: dataOverview
        },
        {
          path: '/projectApply',
          name: 'projectApply',
          component: projectApply
        },
        {
          path: '/projectExamine',
          name: 'projectExamine',
          component: projectExamine
        },
        {
          path: '/costAdmin',
          name: 'costAdmin',
          component: costAdmin
        },
        {
          path: '/invoiceExamine',
          name: 'invoiceExamine',
          component: invoiceExamine
        },
        {
          path: '/invoiceApply',
          name: 'invoiceApply',
          component: invoiceApply
        },
        {
          path: '/refundAdmin',
          name: 'refundAdmin',
          component: refundAdmin
        },
        {
          path: '/operationLog',
          name: 'operationLog',
          component: operationLog
        },
        {
          path: '/test',
          name: 'test',
          component: test
        }
      ]
    }
  ]
})
