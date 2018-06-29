import {Data} from './data/data'
var axios = require('axios')
var MockAdapter = require('axios-mock-adapter')

let _Data = Data

export default {
  init () {
    var mock = new MockAdapter(axios)

    mock.onGet('/data/list/').reply(config => {
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          resolve([200, {
            Data: Data,
            config: config.params
          }])
        }, 500)
      })
    })

    mock.onGet('/data/listPage/').reply(config => {
      let {page, title} = config.params
      let mockData = _Data.filter(Data => {
        if (title && Data.remark.indexOf(title) === -1) return false
        return true
      })
      let total = mockData.length
      mockData = mockData.filter((u, index) => index < 10 * page && index >= 10 * (page - 1))
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          resolve([200, {
            total: total,
            data: mockData
          }])
        }, 1000)
      })
    })
  }
}
