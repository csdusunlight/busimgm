/* 审核option */
export let examineOption = [
  {
    value: '0',
    label: '待审核'
  },
  {
    value: '1',
    label: '审核通过'
  },
  {
    value: '2',
    label: '审核未通过'
  }
]

/* 审核解析过滤 */
export let examineFilter = {0: '待审核', 1: '审核通过', 2: '审核未通过'}

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
    value: '0',
    label: '预付款'
  },
  {
    value: '1',
    label: '后付款'
  }
]

/* 结算方式过滤 */
export let settlewayopsFilter = {0: '预付款', 1: '后付款'}
