>>> from wxautoapi import WeChat

# 登录微信（已登录的微信请先退出）
>>> wx = WeChat()
成功启动微信：1804，等待登录...
微信已登录 (<wxid_xxxxxxxxxxxxx>, XXXX)>>>>>>>

# ======================= 注意！ =======================

# 请确保微信已登录后，再运行下述步骤，否则无法正常调用相关方法！！！
# 请确保微信已登录后，再运行下述步骤，否则无法正常调用相关方法！！！
# 请确保微信已登录后，再运行下述步骤，否则无法正常调用相关方法！！！

# ======================= 注意！ =======================

# 文件传输助手
>>> wx.filehelper.send_text('你好！')
>>> wx.filehelper.send_file('D:/test.txt')

# 查找好友
# 方法一（不知道wxid）：查找备注为张三的好友
>>> person = wx.find_person(by='remark', value='张三')
>>> person.send_text('你好~')
# 方法二（知道wxid）：
>>> person = wx['wxid_xxxxxxxx']

# 查找群（查找备注为工作1群的微信群）
>>> group = wx.find_group(by='remark', value='工作1群')
>>> group.send_text('大家好')

# 获取消息
>>> Messages = wx.getmsgs()
>>> Messages  # 返回一个消息列表，包含所有消息对象
[<WeChat TextMessage Element at 0x2a2781e16a0>,
 <WeChat ImageMessage Element at 0x2a276d7dc18>,
 <WeChat Other Message Element at 0x2a276d7dba8>,
 <WeChat TextMessage Element at 0x2a276d7dc50>,
 <WeChat TextMessage Element at 0x2a276d7d908>]
>>> msg = Messages[0]
>>> msg.text # 消息内容
"xxxxx"