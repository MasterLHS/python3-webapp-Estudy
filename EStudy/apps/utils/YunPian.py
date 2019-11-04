import requests
import json

def send_single_sms(apikey, code, mobile):
    #发送单条短信
    url = "https://sms.yunpian.com/v2/sms/single_send.json"
    text = "【技术开发分享】您的验证码是: {}。如非本人操作，请忽略本短信".format(code)

    res = requests.post(url, data={
        "apikey": apikey,
        "mobile": mobile,
        "text": text
    })

    re_json = json.loads(res.text)

    return res_json

if __name__ == "main":
    re = send_single_sms("74781608422f15b077bea547672ec55c", "123456", "")

    import json
    res_json = json.loads(re.text)
    code = res_json["code"]
    msg = res_json["msg"]
    if code == 0:
        print("发送成功")
    else:
        print("发送失败: {}".format(msg))

    print(re.text)