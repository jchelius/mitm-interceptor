sudo mkdir /sys/fs/cgroup/net_cls
sudo mount -t cgroup -onet_cls net_cls /sys/fs/cgroup/net_cls
sudo mkdir /sys/fs/cgroup/net_cls/e2ee
sudo sh -c 'echo 0x00110011 > /sys/fs/cgroup/net_cls/e2ee/net_cls.classid'
