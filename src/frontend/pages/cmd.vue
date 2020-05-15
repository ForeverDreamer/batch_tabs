<template>
  <div class="container">
    <h1 class="text-center">欢迎使用后台管理工具</h1>
    <div class="d-flex justify-content-around align-items-center">
      <el-button type="primary" class="w-25" @click="collectstatic">
        collectstatic
      </el-button>
      <el-button type="primary" class="w-25" @click="migrate">
        migrate
      </el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cmd',
  methods: {
    collectstatic() {
      this.$axios
        .post('/cmd/collectstatic/')
        .then((response) => {
          this.$message({
            message: '命令执行成功!',
            type: 'success'
          })
        })
        .catch((error) => {
          this.$alert(error + ', 请联系客服处理!', '程序错误', {
            confirmButtonText: '确定'
          })
        })
    },
    migrate() {
      this.$axios
        .post('/cmd/migrate/')
        .then((response) => {
          this.$message({
            message: '命令执行成功!',
            type: 'success'
          })
        })
        .catch((error) => {
          this.$alert(error + ', 请联系客服处理!', '程序错误', {
            confirmButtonText: '确定'
          })
        })
    }
  }
}
</script>

<style scoped></style>
