import base64
import hashlib
import json

def getBase64(data: bytes) -> str:
    assert type(data) == bytes
    return base64.b64encode(data).decode("ascii")

def getBase64Decode(b64: str) -> bytes:
    assert type(b64) == str
    return base64.b64decode(b64)

def getMd5(data: bytes) -> str:
    assert type(data) == bytes
    md5 = hashlib.md5()
    md5.update(data)
    return md5.hexdigest().lower()

def sign(data: bytes, password: bytes) -> bytes:
    assert type(data) == bytes
    assert type(password) == bytes
    container = {
        "data": getBase64(data),
        "sign": getMd5(password + data + password)
    }
    return json.dumps(container).encode()

def checkSign(signed_data: bytes, password: bytes) -> bytes:
    assert type(signed_data) == bytes
    assert type(password) == bytes
    try:
        dic = json.loads(signed_data.decode())
        assert type(dic) == dict
        assert dic.get("data") is not None
        assert dic.get("sign") is not None
        raw_data = getBase64Decode(dic["data"])
        sign     = dic["sign"]
        assert sign == getMd5(password + raw_data + password)
        success = True
    except:
        success = False
    return success

if __name__ == "__main__":
    signed_data = sign(b"hello world", b"ggn_2015")
    print(checkSign(signed_data, b"ggn_2014"))
    print(checkSign(signed_data, b"ggn_2015"))