#!/usr/bin/env python3
# coding: utf-8
# Author: colin
# Mail: icesky624@hotmail.com
# Write Time: 19-2-27
# 用来获取斗鱼相关弹幕
import socket
import re
import threading
import time


class Danmu(object):
    def __init__(self, roomid):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.codeLocalToServer = 689
        self.serverToLocal = 690
        self.gid = -9999
        self.host = "openbarrage.douyutv.com"
        self.port = 8601
        self.roomid = roomid

    def sendmsg(self, msg):
        msg = msg.encode('utf-8')
        data_length = len(msg) + 8
        msg_head = int.to_bytes(data_length, 4, 'little') + int.to_bytes(data_length, 4, 'little') + int.to_bytes(
            self.codeLocalToServer, 4, 'little')
        self.sock.send(msg_head)
        self.sock.sendall(msg)

    def login(self):
        msg = 'type@=loginreq/roomid@=' + str(self.roomid) + '\0'
        self.sock.connect((self.host, self.port))
        self.sendmsg(msg)

    def join(self):
        msg = 'type@=joingroup/rid@=' + str(self.roomid) + '/gid@=' + str(self.gid) + '\0'
        self.sendmsg(msg)

    def keeplive(self):
        while True:
            localtime = time.time()
            msg = 'type@=keepalive/tick@{}\0'.format(localtime)
            self.sendmsg(msg)
            time.sleep(15)

    def recv(self):
        while True:
            data = self.sock.recv(1024)
            self.getdanmu(data)

    def getdanmu(self, danummus):
        text = re.search(b'type@=(\w*)', danummus)
        if text:
            if text.group(1) == b'chatmsg':
                danmu = re.search(b'nn@=(.*)/txt@=(.*?)/ci.*/level@=(\d+)/', danummus)
                try:
                    print("Level" + "%02s" % (danmu.group(3).decode()) + " " + danmu.group(
                        1).decode() + ' 说: ' + danmu.group(2).decode())
                # except BaseException as e:
                #     pass


if __name__ == '__main__':
    room = input("来来，随便输入一个直播间看精彩弹幕：(默认房间号32892) ")
    room = 32892 if room=='' else room
    danmu = Danmu(room)
    danmu.login()
    danmu.join()
    threading.Thread(target=danmu.keeplive).start()
    danmu.recv()
