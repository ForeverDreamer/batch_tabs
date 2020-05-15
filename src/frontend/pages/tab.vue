<template>
  <div class="container">
    <h1 class="text-center">欢迎使用批量打开网页工具</h1>
    <p>请配置需要打开的网址，每个网址占一行：</p>
    <el-form ref="form" :model="form" label-width="0px">
      <el-form-item>
        <el-input
          v-model="form.textarea"
          type="textarea"
          :rows="22"
          placeholder="请输入网址"
        >
        </el-input>
      </el-form-item>
      <el-form-item>
        <div class="d-flex justify-content-around align-items-center">
          <el-button type="primary" class="w-25" @click="openTabs">
            批量打开网页
          </el-button>
          <!--          <el-button type="primary" class="w-25" @click="collectstatic">-->
          <!--            collectstatic-->
          <!--          </el-button>-->
          <!--          <el-button type="primary" class="w-25" @click="migrate">-->
          <!--            migrate-->
          <!--          </el-button>-->
        </div>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'Tab',
  data() {
    return {
      form: {
        textarea: ''
      }
    }
  },
  mounted() {
    this.init()
  },
  methods: {
    init() {
      this.$axios
        .get('/url/restore/')
        .then((response) => {
          console.log(response)
          const urls = response.data.urls
          if (urls.length === 0) {
            const placeholders = [
              '示例网址：',
              'https://www.sina.com.cn/',
              'https://www.baidu.com',
              'https://sohu.com'
            ]
            this.form.textarea = placeholders.join('\n')
          } else {
            this.form.textarea = urls.join('\n')
          }
        })
        .catch((error) => {
          this.$alert(error + ', 请联系客服处理!', '程序错误', {
            confirmButtonText: '确定'
          })
        })
    },
    openTabs() {
      let urls = this.form.textarea.split('\n')
      urls = urls.map((value) => value.trim())
      urls = urls.filter(function(value, index, array) {
        return value !== ''
      })
      this.$axios
        .post('/url/open/', { urls })
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
