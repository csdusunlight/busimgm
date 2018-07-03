/* 审核option */
export let examineOption = [
  {
    value: '0',
    label: '审核通过'
  },
  {
    value: '1',
    label: '未审核'
  },
  {
    value: '2',
    label: '审核失败'
  }
]

/* 审核解析过滤 */
export let examineFilter = {0: '审核通过', 1: '未审核', 2: '审核失败'}

/* 对公对私option */
export let paccounOption = [
  {
    value: '1',
    label: '对私'
  },
  {
    value: '0',
    label: '对公'
  }
]

/* 对公对私解析过滤 */
export let paccountypeopsFilter = {0: '对公', 1: '对私'}

/* 结算方式option */
export let settlewayopsoption = [
  {
    value: 'advance',
    label: '预付款'
  },
  {
    value: 'later',
    label: '后付款'
  }
]

/* 结算方式过滤 */
export let settlewayopsFilter = {advance: '预付款', later: '后付款'}
