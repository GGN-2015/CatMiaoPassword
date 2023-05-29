import NetworkUtils
import SignUtils

ret = NetworkUtils.sendTCP("127.0.0.1", 33278, 
                           SignUtils.sign(b"hi", b"ikun_114514_1919810"))
print(ret)