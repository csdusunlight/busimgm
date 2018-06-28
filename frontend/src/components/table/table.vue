<template>
  <el-table
    @sort-change="sortChange"
    :data="data">
    <template v-for="colConfig in colConfigs">
      <slot v-if="colConfig.slot" :name="colConfig.slot">
        <el-table-column v-bind="colConfig"></el-table-column>
    </template>
  </el-table>
</template>

<script>

export default {
  props: ['colConfigs', 'data'],
  methods: {
    sortChange (val) {
      console.log(val)
    }
  }
}
</script>

<style>
</style>
