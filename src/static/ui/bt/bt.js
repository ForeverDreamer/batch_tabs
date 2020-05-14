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
                    console.log(error)
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
                    console.log(response)
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        collectstatic() {
            axios
                .post('/cmd/collectstatic/')
                .then((response) => {
                    console.log(response)
                })
                .catch((error) => {
                    console.log(error)
                })
        },
        migrate() {
            axios
                .post('/cmd/migrate/')
                .then((response) => {
                    console.log(response)
                })
                .catch((error) => {
                    console.log(error)
                })
        }
    }
})