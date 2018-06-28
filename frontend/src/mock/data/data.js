import Mock from 'mockjs'

const Data = []

for (let i = 0; i < 93; i++) {
  Data.push(Mock.mock({
    'id': i,
    date: Mock.Random.datetime(),
    date2: Mock.Random.datetime(),
    name: Mock.Random.cname(),
    number: Mock.Random.integer(100000000000, 10000000000000),
    img: Mock.Random.dataImage('400x400'),
    string: Mock.Random.csentence(4, 10),
    string2: Mock.Random.csentence(12, 20),
    qq_number: Mock.Random.integer(1000000, 10000000000),
    integer: Mock.Random.integer(100, 1000),
    integer2: Mock.Random.integer(0, 100),
    float: Mock.Random.float(0, 100000, 1, 2),
    remark: Mock.Random.cparagraph(1, 3),
    'state|1': ['已通过', '未审核', '已拒绝']
  }))
}

export {Data}
