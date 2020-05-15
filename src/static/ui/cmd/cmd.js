new Vue({
    el: '#app',
    data() {
        return {
            form: {
                textarea: ''
            }
        }
    },
    methods: {
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