# PUSH SDK

## 要解决什么问题
在Android上实现Push Message。现在是一件非常复杂的事，以前可能使用一家第三方Push平台，就能解决。如今却发现在 华为，小米手机上出现问题。所以要解决的问题是 **“尽可能提高到达率”**。

### 收不到推送的原因
1. 由于Android系统的机制，后台推送 Service 会被各种主动的或是被动的行为给杀死，而服务一旦被杀死，意味着就接收不到推送消息。
2. 即使推送Service收到了消息，由于系统、安全软件、手机管家等限制，消息无法到达App。
3. 由于手机厂商的定制系统，限制了第三方服务的 **“保活”**和 **“互拉”**

### 解决问题
大体思路就是，针对小米，华为系统，使用对应Push SDK。其他手机使用第三方Push平台。

区分Notification 和 Payload ，对不同业务，做不同处理。

---

## 选择第三方Push平台
以下列出常见第三方Push平台（排名不分先后）：

- 手机厂商：
    - 小米
    - 华为
- 专业第三方平台：
    - 友盟
    - 极光
    - 个推
    - 云巴
- BAT平台：
    - 阿里云
    - 腾讯信鸽
    - 百度云
  
### 各平台特点

 - 厂商：他们的推送服务在他们自己生产的手机上属于系统级别的服务。
 - 专业第三方：“保活”和“互拉”，共享推送通道。
 - BAT大厂：没什么优势，用了信鸽也沾不上微信的光。手机淘宝也使用了友盟推送。

#### 厂商
他们的推送服务在他们自己生产的手机上属于系统级别的服务，理论上来说，手机系统对他们自家的推送限制最小。

比如，在小米手机上，不在系统自启动名单里的App，在手机重启后，App声明的后台Service并不会自动运行。但是，小米推送作为手机系统级服务，仍然是可以收到推送的。

同样，华为推送的技术团队也对外宣称（原话）：
> 华为Push，在华为手机上是系统级别的服务，稳定性等各方面肯定都会好些。

#### 专业第三方
他们的优势在于 **“保活”** 和 **“互拉”**。

举个例子，假设你接入了友盟，而恰好今日头条也接入了友盟。有一天你的App被杀死了，但是今日头条的装机量估计比你的要大啊，这时用户启动了今日头条，那么推送系统也就会通过共享的推送通道顺便把你推送消息送达到手机上，然后还可能把你的进程也唤醒（被“保活”了）。
 
#### BAT大厂
 从原理上，除了手机厂商外的Push方案，都是要看 **“保活”** 和 **“互拉”**。
 
 BAT有自己的大流量APP，比如微信，如果能被微信拉起肯定是很美好的。但实际上，测试后，没用。
 
 再比如手机淘宝，里面有使用友盟推送。
 
#### 有意思的是。。。
但是，即使是系统级别的推送服务，也不是百分百保证消息送达。这里比较奇葩的是华为推送，下面是他们技术支持给出的描述（原话） 
> 华为手机上：
Emui3.0上，Push广播有很大概率被限制，如： Mate7 3.0版本，荣耀6plus，P7 3.0版本，4X， 4A等。
Emui3.1上，Push广播基本不被限制，但个别型号机型存在问题，如：荣耀5x等。
Emui4.0及以上，Push广播有较高概率被限制，不被限制的机型如：荣耀畅玩4C，荣耀畅玩4X，Mate S，P8 MAX等。
如广播被限制，需要将应用设为开机启动项。所以对于及时性或到达率要求非常高的应用，我们建议应用要考虑替代方案。
后续Push版本，华为将采用新的设计方案，解决被限制的问题，但发布计划待定。

另外，至于限制的问题，其实华为sdk还是能接收到推送消息的，当将消息通过广播发送给应用，如果手机管家查到该应用处于stop状态，那么会拦截该广播的。

---

## 如何选择第三方Push平台？
既然选择第三方，是看重它们的 **“保活”** 和 **“互拉”**，那就要看它们的规模了。我会从3个方面来考虑。
- 一些渠道的app统计
- 看官网上合作案例
- 自己写demo，直接测试。

某平台做的统计，适当参考
![image](http://static.open-open.com/lib/uploadImg/20160711/20160711152842_976.jpg)

#### 合作案例
小米PUSH：
![image](https://github.com/ddaitest/PushCollector/blob/master/res/mi_1.png?raw=true)

个推：
![image](https://github.com/ddaitest/PushCollector/blob/master/res/gt_1.png?raw=true)
![image](https://github.com/ddaitest/PushCollector/blob/master/res/gt_2.png?raw=true)
![image](https://github.com/ddaitest/PushCollector/blob/master/res/gt_3.png?raw=true)

友盟：
![image](https://github.com/ddaitest/PushCollector/blob/master/res/umeng_1.png?raw=true)
![image](https://github.com/ddaitest/PushCollector/blob/master/res/umeng_2.png?raw=true)
![image](https://github.com/ddaitest/PushCollector/blob/master/res/umeng_3.png?raw=true)

### 各平台测试

测试5个Push平台：华为、小米、个推、友盟、腾讯个推。并实现 Client & Server。

- Client (PushCollector)：注册&激活各SDK，上传各Token到Server，收集Payload消息。
- Server：收集Token，同时发送Notification/Payload 到指定平台。

全部代码：[https://github.com/ddaitest/PushCollector](https://github.com/ddaitest/PushCollector)

Client 下载地址： [http://daivp.com](http://daivp.com)

Server 发消息地址： [http://daivp.com/queen/write](http://daivp.com/queen/write)

测试结果：[https://github.com/ddaitest/PushCollector/blob/master/test_result.md](https://github.com/ddaitest/PushCollector/blob/master/test_result.md)


### 概念 & 原理
专业第三方Push平台，Push流程，标出个阶段对到达率的影响。

![image](https://github.com/ddaitest/PushCollector/blob/master/res/flow.png?raw=true)

#### Notification & Payload
Android Push分为**通知栏 (Notification)** 和**透传 (Payload)**。

Notification不用app处理，由系统推送服务/共享推送通道处理。所以成功率高。
Payload 还需要再路由到app，如果app不能启动，及失败。

所以两者送达率不同。比如小米官方描述。
> 在一些 Android 系统(如 MIUI)中,受到系统自启动管理设置的限制,应用不能在后台自启动。在这类系统中,如果在发送消息的时候对应的应用没有被启动,透传类消息将不能顺利送达。因此,对于对送达率要求很高的消息,建议尽量采用通知栏提醒的方式推送消息

#### Broadcast & Token List & Tag
调用Push API 发送消息的几种参数。
- Broadcast - 发送到全部用户。
- Token List - 指定设备。
- Tag - 绑定部分设备为tag，用于批量发送。


## 各厂商常见问题

### 华为
华为push现升级为HMS,但不稳定和完善，比如：

- 可能安装/升级华为移动服务，会弹窗。
- 推送的api，不支持tag，只能指明user token。
- 全部推送的api，官方不推荐使用，且将下线。
- 推送每次最多1000设备。


即使集成了像华为和小米这样的系统级别的推送，也不一定百分百收到消息，即使你在系统设置了自启动，因为有时候你设置了自启动，但是依然不在系统的自启动白名单中。

华为系统只有设置了自启动，系统才会考虑拉起应用，系统在接收到推送消息以后，会检查一下自己的系统中的自启动白名单，白名单中放置了所谓的设置过自启动的包名，如果推送消息的包名和不在白名单中，操作系统是不会拉起应用的。（注意，即使你设置了自启动，也不一定在白名单中，你最好看一下系统的日志，把整个推送到达后的系统如何进行处理的日志全部看一下，你就会发现问题在哪里）

### 友盟
[引用官方](http://bbs.umeng.com/thread-21334-1-1.html)

集成Android SDK的过程中，不少厂商会定制化ROM，导致有的时候推送不能很好的工作，比如小米机型。给开发者朋友们造成了很大的困扰(其实定制ROM给第三方推送也带来了很多适配上的麻烦), 如下是我们整理出来的目前市场上对友盟推送会造成限制的机型列表，也欢迎广大开发者为我们反馈新的问题机型，我们会不定期更新这个列表:

注：需要使用消息路由功能，要按照下面的方式设置： 
小米【MIUI7、MIUI8】
       安全中心-授权管理-自启动管理，需把应用添加到允许自启动列表里
华为【EMUI 4】
       手机管家-权限管理-自启动管理-关联启动，需允许应用被其他应用启动
      （首次触发相互唤醒后，应用才会出现在关联启动的应用列表里）
魅族
       【Flyme 5】
        手机管家-权限管理-自启动管理-相互启动，需允许相互启动
      （Flyme 5.1.9.0A及以上版本没有相互启动选项，只有自启动选项，需允许自启动）
       【Flyme 6】
        手机管家-后台管理，应用需勾选保持后台运行
VIVO【Funtouch OS_2.5】
       i管家-软件管理-自启动管理-关联启动，需允许应用的关联启动
      （首次触发相互唤醒后，应用才会出现在关联启动的应用列表里）
努比亚【Nubia UI v3.7.8及以上】
       手机管家-授权管理-自启动管理，需允许自启动


---
## 引用
[国内Top500Android应用分析报告](http://www.open-open.com/lib/view/open1468222124208.html)

[集成Android推送前必看](http://www.jianshu.com/p/017096be88da)

[集成华为推送那些坑](http://www.jianshu.com/p/47a6826f9815)

[微爱cto总结Android 端外推送到底有多烦？](https://juejin.im/post/57a19c012e958a0066715d0c)

[推送“送达率”概念太模糊？友盟带你解读“送达率”背后的那些指标](http://blog.umeng.com/%E5%B7%A5%E7%A8%8B%E6%8A%80%E6%9C%AF/4541.html)

[Android 第三方 Push 推送方案使用调查](https://github.com/android-cn/topics/issues/4#issuecomment-223264673)

[华为官方：Push SDK-客户端常见问题](http://club.huawei.com/thread-10205061-1-1-2851.html)