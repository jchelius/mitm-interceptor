import random
import string
import socket
import subprocess
import os

def main():
    TOKEN_LEN = 20
    token = rand_str(TOKEN_LEN)
    rand_msgs = gen_rand_msgs(20,token)

    # create the cgroups directory
    cgroup_net_cls_dir = '/sys/fs/cgroup/net_cls'
    cgroup_name = 'e2ee'
    cgroup_id = '0x00110011'
    cgroup_dir = create_cgroups_dir(cgroup_net_cls_dir, cgroup_name, cgroup_id)
    # add pid to custom net_cls cgroup
    add_proc_to_cgroup(cgroup_dir)
    # set the netfilter rules
    set_nf_rules(cgroup_id)
    # start the mitmproxy
    fake_ciphertext = 'FAKE_CIPHERTEXT'
    cmd_str = f'sudo -u mitmproxyuser -H bash -c \"\$HOME/.local/bin/mitmdump --mode transparent --set block_global=false --quiet --modify-body /~q/{token}/{fake_ciphertext}\"'
    subprocess.run(cmd_str, shell=True)
    
    send_all_msgs(rand_msgs)
    # print(rand_msgs)

def create_cgroups_dir(cgroup_net_cls_dir, cgroup_name, cgroup_id):
    if not os.path.exists(cgroup_net_cls_dir):
        os.mkdir(cgroup_net_cls_dir)
    cgroup_dir = cgroup_net_cls_dir + '/' + cgroup_name
    if not os.path.exists(cgroup_dir):
        os.mkdir(cgroup_dir)
    print(cgroup_dir)
    cmd_str = f'sudo sh -c \'echo {cgroup_id} > {cgroup_dir}/net_cls.classid\''
    subprocess.run(cmd_str, shell=True)
    return cgroup_dir

def add_proc_to_cgroup(cgroup_dir):
    pid = os.getpid()
    cmd_str = f'sudo sh -c \'echo {pid} > {cgroup_dir}/cgroup.procs\''
    subprocess.run(cmd_str, shell=True)

def set_nf_rules(cgroup_id):
    cmds = [f'sudo iptables -t nat -A OUTPUT -p tcp -m cgroup --cgroup {cgroup_id} -m owner ! --uid-owner mitmproxyuser --dport 80 -j REDIRECT --to-port 8080', f'sudo iptables -t nat -A OUTPUT -p tcp -m cgroup --cgroup {cgroup_id} -m owner ! --uid-owner mitmproxyuser --dport 443 -j REDIRECT --to-port 8080', f'sudo ip6tables -t nat -A OUTPUT -p tcp -m cgroup --cgroup {cgroup_id} -m owner ! --uid-owner mitmproxyuser --dport 80 -j REDIRECT --to-port 8080',f'sudo ip6tables -t nat -A OUTPUT -p tcp -m cgroup --cgroup {cgroup_id} -m owner ! --uid-owner mitmproxyuser --dport 443 -j REDIRECT --to-port 8080']
    for cmd in cmds:
        subprocess.run(cmd, shell=True)

def send_all_msgs(msgs):
    HOST = 'byu.edu'
    PORT = 80
    for msg in msgs:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
        # for msg in msgs:
            s.sendall(bytes(msg, 'utf-8'))
    print(f"sent all {len(msgs)} messages")

def rand_str(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def gen_rand_msgs(n, token):
    L = 100
    res = []
    for i in range(n):
        rand_msg = rand_str(L)
        if 2*i > n:
            index = random.randint(0,len(rand_msg)-len(token)-1)
            rand_msg = rand_msg[:index] + token + rand_msg[index + 1:]
            # print(rand_msg)
        res.append(rand_msg)
    return res

if __name__ == '__main__':
    main()
