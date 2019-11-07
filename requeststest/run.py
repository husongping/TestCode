"""
    1、读取excel中的测试用例
    2、循环读取执行每一个测试用例

"""
from utils.excel_tool import read_excel
import requests
#1、读取excel
sheet_name = "注册模块"
excel_path = "D:\\testcode\\requeststest\\cases\\lux项目接口测试用例.xlsx"
res = read_excel(excel_path,sheet_name)
# print(res)

#循环执行每一个测试用例
for i in res:           #循环读取
    #2.1取出所需要的参数
    url = i[3]           #获取接口的地址
    data = eval(i[5])   #请求的数据
    method = i[4]       #http的请求方法
    http_code = i[6]    #http的响应状态码
    result_code = i[7]  #响应值的状态码

    case_name = i[1]    #测试用例的名字

    #2.2构造请求,所有的请求数据都是通过excel里面动态读取出来的
    r = requests.request(method = method,url = url,json = data)
    #2.3断言http响应状态码
    try:

        assert r.status_code == http_code

        #2.4断言返回值
        assert result_code in r.text
        
        print("测试用例【{}】执行通过".format(case_name))
    except:
        print("测试用例【{}】执行失败，\n预期响应码：{}，\n实际响应码{}，\n返回结果{}".format(case_name,http_code,r.status_code,r.text))