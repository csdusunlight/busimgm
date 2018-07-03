import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const state = {
  username: '',
  jurisdiction: {}
}

const getters = {
  username: state => state.username,
  jurisdiction: state => state.jurisdiction
}

const actions = {
  addUserName ({ commit, state }, name) {
    commit('modifySubaccount', name)
  },
  jurisdictionRow ({ commit, state }, obj) {
    commit('tubejurisdiction', obj)
  }
}

const mutations = {
  modifySubaccount (state, data) {
    state.username = data
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
