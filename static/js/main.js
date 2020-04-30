$(function () {
    // let和const是es6的语法，有些老版本的浏览器不支持，es5不要使用，只能使用var
    // 但是2017下半年发布的浏览器版本都支持es6，到现在3年多了，没必要写es5太麻烦，容易出错
    // 如果有问题，提示用户升级浏览器版本就好
    let urls
    $('#openBtn').click(event => {
        urls = $('textarea').val().split('\n')
        urls = urls.map(value => value.trim())
        urls = urls.filter(function (value, index, array) {
            return value !== ''
        })
        // const axios = require('axios');
        axios.post('/url/open/', { urls })
            .then( response => {
                console.log(response);
            })
            .catch( error => {
                console.log(error);
            });
    })
    axios.get('/url/restore/')
        .then( response => {
            console.log(response);
            urls = response.data.urls
            $('textarea').val(urls.join('\n'))
        })
        .catch( error => {
            console.log(error);
        });
})