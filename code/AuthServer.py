import json
import NetworkUtils
import SignUtils
import ConfigUtils

SERVER_IP   = ConfigUtils.get("SERVER_IP")
SERVER_PORT = ConfigUtils.get("SERVER_PORT")
AUTH_TOKEN  = ConfigUtils.get("AUTH_TOKEN").encode()

def __make_msg(v: dict) -> bytes:
    return json.dumps(v).encode()

SIGN_WRONG_MESSAGE = __make_msg({"type": "SIGN_WRONG_MESSAGE"})

def fileWorker(client_signed_data: str):
    if not SignUtils.checkSign(client_signed_data, AUTH_TOKEN):
        return SIGN_WRONG_MESSAGE
    else:
        client_data = SignUtils.getClientDataFromSignedData(client_signed_data) # bytes
        return b"not implemented"
        
if __name__ == "__main__":
    NetworkUtils.startDemoServerTCP(SERVER_IP, SERVER_PORT, fileWorker)
