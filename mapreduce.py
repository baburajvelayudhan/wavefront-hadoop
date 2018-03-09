import argparse
import urllib2
import json
import datetime

def doMain():
    url = '%s/ws/v1/cluster/apps/' % args.server
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    if "apps" in data:
        apps = []
        for app in data["apps"]["app"]:
            if valid(int(app["finishedTime"]/1000.0)) :
                apps.append(app)
        print(json.dumps(apps, ensure_ascii=False))

def valid(finishedTime):
    seconds = (datetime.datetime.now() - datetime.datetime.fromtimestamp(finishedTime)).seconds
    if (finishedTime != 0) and (seconds >= 300):
        return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('server', type=str, nargs='?', help='ResourceManager Server URL')
    parser.add_argument('--username', type=str, nargs='?', help='ResourceManager Server user.')
    parser.add_argument('--password', type=str, nargs='?', help='ResourceManager Server password.')

    args = parser.parse_args()

    if args.username:
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, args.server, args.username, args.password)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)

    if not args.server:
        parser.error('server must be provided')
    doMain()
