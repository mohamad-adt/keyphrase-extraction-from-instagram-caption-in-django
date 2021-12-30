import os
import instaloader

############################# LOAD SESSION AND GET USER PROFILE ##############################
def GetUserProfile(UsrName):
    L = instaloader.Instaloader()
    L.load_session_from_file('nsisheken')
    posts = instaloader.Profile.from_username(
        L.context, UsrName).get_posts()
    return posts

############################ GET DISCRIPTION FROM POSTS #################################
def GetDiscription(posts:str):
    caps = ""
    for post in posts:
        caps += str(post.caption) + "\n"
    return caps

# print(type(caps))

############################ SAVE DISCRIPTION IN TXT FILE ##############################
def Save_Discription(caps):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_PATH = os.path.join(ROOT_DIR, 'File.txt')
    f = open(FILE_PATH, "w", encoding="utf-8")
    f.write(caps)
    f.close()

################ MAIN #################
def main(UsrName):
    posts = GetUserProfile(UsrName=UsrName)
    caps = GetDiscription(posts)
    Save_Discription(caps)
    return caps


if __name__ == '__main__':
    main(UsrName= input('Please Enter Username: '))
