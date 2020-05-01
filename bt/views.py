from django.shortcuts import render


def home_view(request):
    ph_list = ('示例网址：', 'sina.com', 'http://www.baidu.com', 'https://souhu.com')
    # placeholder = '示例网址：' + '\n' + 'sina.com' + '\n' + 'http://www.baidu.com' + '\n' + 'https://souhu.com'
    placeholder = '\n'.join(ph_list)
    print(placeholder)
    data = {'placeholder': placeholder}
    return render(request, "bt/home.html", data)
