# jkdk

## 郑州大学健康打卡

---

## 使用方法

1. 先把代码整个都clone下来，然后在此基础上自己创建一个github仓库，仓库设置为私人。或者把代码fork到你自己的仓库（不过这样改不了仓库的可见性为私人）

![fork截图](./images/fork.png)

2. 点击settings，找到Secrets

![settings](./images/settings.png)

3. 添加2个仓库密钥 username和password，分别表示学号和密码

![添加仓库密钥](./images/secret.png)

![添加学号](./images/username.png)

添加学号，name必须是username
密码的添加同理，但name必须是password
添加所在地理位置，省的name必须是province，value是参考
https://gist.github.com/mayufo/4207ed3fa925e6b3df7559832af85165，
是所对应数字的前两位，城市的name必须是city，value是上面链接对应数字的第三、四位
详细地址就没有要求，但是name必须是position

4. 结束。接下来会每日6点、6点10分和7点、7点10分自动打卡（多次打卡防止打卡失败）

---

## 添加微信通知的方法

1. 注册 https://cp.xuthus.cc/ 这个网站，然后再增强里面，下滑到微信推送，绑定微信账号

2. 把调用代码SKEY保存下来，按照上文添加学号密码的方法，添加到secrets中，其中Name是key，value是你的SKEY

   ![skey](./images/SKEY.png)

3. 按照网站所说，关注微信号，最后成功添加微信通知。
