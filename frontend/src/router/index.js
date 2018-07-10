import Vue from 'vue'
import Router from 'vue-router'

const projectOverview = () => import('@/components/projectOverview/projectOverview')
const projectLive = () => import('@/components/projectLive/projectLive')
const dataAdmin = () => import('@/components/dataAdmin/dataAdmin')
const dataOverview = () => import('@/components/dataOverview/dataOverview')
const projectApply = () => import('@/components/projectApply/projectApply')
const projectExamine = () => import('@/components/projectExamine/projectExamine')
const costApply = () => import('@/components/costApply/costApply')
const costExamine = () => import('@/components/costExamine/costExamine')
const invoiceExamine = () => import('@/components/invoiceExamine/invoiceExamine')
const invoiceApply = () => import('@/components/invoiceApply/invoiceApply')
const refundApply = () => import('@/components/refundApply/refundApply')
const refundExamine = () => import('@/components/refundExamine/refundExamine')
const operationLog = () => import('@/components/operationLog/operationLog')
const login = () => import('@/components/login/login')

const routerAdmin = () => import('@/components/routerAdmin/routerAdmin')
const test = () => import('@/components/test/test')

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/routerAdmin'
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
          path: '/costApply',
          name: 'costApply',
          component: costApply
        },
        {
          path: '/costExamine',
          name: 'costExamine',
          component: costExamine
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
          path: '/refundApply',
          name: 'refundApply',
          component: refundApply
        },
        {
          path: '/refundExamine',
          name: 'refundExamine',
          component: refundExamine
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
