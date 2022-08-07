import requests

# 이미지가 있는 url 주소
url = "image url"

# 해당 url로 서버에게 요청
img_response = requests.get(url)

# 요청에 성공했다면,
if img_response.status_code == 200:
    #print(img_response.content)

    print("========= [이미지 저장] =========")
    with open("test.jpg", "wb") as fp:
        fp.write(img_response.content)