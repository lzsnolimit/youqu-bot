from chirpsdk import ChirpConnect, CallbackSet

# 初始化Chirp连接对象
connect = ChirpConnect()

# 将数据转为Chirp编码
payload = 'Your WiFi Password'.encode('utf8')  # 将WiFi密码转为bytes
chirp = connect.new_payload(payload)  # 创建新的Chirp编码

# 播放Chirp编码
connect.start(send=True)
connect.send(chirp)

# 当Chirp播放完毕后，关闭Chirp连接
connect.close()