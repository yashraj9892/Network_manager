import urllib.request as req
import subprocess
import ssl
import urllib.parse as ub
ssl._create_default_https_context = ssl._create_unverified_context


def send_request(request_type, BASE_URL,arg):
    if(request_type == 'login'):
        params = ub.urlencode({'mode': 191, 'username': arg[0], 'password': arg[1]}).encode('utf-8')
    elif(request_type == 'logout'):
        params = ub.urlencode({'mode': 193, 'username': arg[0]}).encode('utf-8')
    try:
        response = req.urlopen(BASE_URL, params,timeout=2)
        return response.read()
    except Exception as e:
        pass

def logout(username,url):
    arg=[]
    arg.append(username)
    data = send_request('logout',url,arg)
    return data
        
def main(value,username,password,url):

    login_check= False
    arg =[]
    arg.append(username)
    arg.append(password)

    try:
        if "Login" in value:
            data = send_request("login",url,arg)
##            print(data)
            if None is data:
                return "Request Failed, Please try again later"
            elif b"maximum" in data:
                return "MAXIMUM LIMIT"
            elif b"exceeded" in data:
                return  "Data Exceeded"
            elif b"could not" in data:
                return "Incorrect username or password"
            elif b"logged in" in data:
                return "Logged in"
            else:
                return "Request Failed, Please try again later"
        else:
             data = logout(username,url)
             return "Logged out Successfully!!"
             
    except KeyboardInterrupt or Exception as e:
        logout(username,url)
        return "Logged out Successfully!!"
        
