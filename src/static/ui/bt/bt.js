new Vue({
    el: '#app',
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
            axios
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
                    });
                })
        },
        openTabs() {
            let urls = this.form.textarea.split('\n')
            urls = urls.map((value) => value.trim())
            urls = urls.filter(function (value, index, array) {
                return value !== ''
            })
            axios
                .post('/url/open/', {urls})
                .then((response) => {
                    this.$message({
                        message: '命令执行成功!',
                        type: 'success'
                    });
                })
                .catch((error) => {
                    this.$alert(error + ', 请联系客服处理!', '程序错误', {
                      confirmButtonText: '确定'
                    });
                })
        },
        collectstatic() {
            axios
                .post('/cmd/collectstatic/')
                .then((response) => {
                    this.$message({
                        message: '命令执行成功!',
                        type: 'success'
                    });
                })
                .catch((error) => {
                    this.$alert(error + ', 请联系客服处理!', '程序错误', {
                      confirmButtonText: '确定'
                    });
                })
        },
        migrate() {
            axios
                .post('/cmd/migrate/')
                .then((response) => {
                    this.$message({
                        message: '命令执行成功!',
                        type: 'success'
                    });
                })
                .catch((error) => {
                    this.$alert(error + ', 请联系客服处理!', '程序错误', {
                      confirmButtonText: '确定'
                    });
                })
        }
    }
})