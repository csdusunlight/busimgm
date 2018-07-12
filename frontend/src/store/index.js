import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const state = {
  username: '',
  userId: '',
  jurisdiction: {}
}

const getters = {
  username: state => state.username,
  userId: state => state.userId,
  jurisdiction: state => state.jurisdiction
}

const actions = {
  addUserName ({ commit, state }, name) {
    commit('modifySubaccount', name)
  },
  addUserId ({ commit, state }, id) {
    commit('getAddUserId', id)
  },
  jurisdictionRow ({ commit, state }, obj) {
    commit('tubejurisdiction', obj)
  }
}

const mutations = {
  modifySubaccount (state, data) {
    state.username = data
  },
  getAddUserId (state, id) {
    state.userId = id
  },
  tubejurisdiction (state, obj) {
    state.jurisdiction = obj
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
