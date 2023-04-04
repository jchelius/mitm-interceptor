from main import *

def main1():
    token = rand_str(20)
    rand_msgs = gen_rand_msgs(20,token)
    send_all_msgs(rand_msgs)

if __name__ == '__main__':
    main1()
