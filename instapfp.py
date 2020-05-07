import requests as req
import sys

user = "g_an"

if len(sys.argv) == 2:
    user = sys.argv[1]
else:
    print("Please add username argument")

def find():
    data = req.get("http://instagram.com/" + user)

    #Find index of pfp url
    start = data.text.find('profile_pic_url_hd')
    end = data.text.find('requested_by_viewer')

    pfpurl = data.text[start+21:end-3]
    return pfpurl

def fixurl():
    #Fix "Bad URL Timestamp" Error
    newurl = find().replace("\\u0026", "&")
    return(newurl)

def dl():
    filename = user + ".jpg"

    r = req.get(fixurl())

    #Read url as str, write to file
    with open(filename, 'wb') as pfp:
        pfp.write(r.content)

def main():
    dl()

if __name__ == "__main__":
    main()