# PUSH SDK

## 概述
### Android 保活
由于Android系统的机制，后台推送 Service 会被各种主动的或是被动的行为给杀死，而服务一旦被杀死，意味着就接收不到推送消息。

### 第三方推送原理


```
sequenceDiagram
APP Server ->> Push Server: 发送总数=100
Push Server->> Push Server: 验证.接受数=99
Push Server->> Phone Tunnel: 下发数=40
Phone Tunnel-->> Push Server: Ack送达，送达设备数=39
Phone Tunnel->> App: 路由，送达APP数=30
```


### 概念
Android 推送分为**端内&端外**。
- 当APP在前台，基于长连接，自己维护一套机制，为端内推送。
- APP退到后台，短时间内可以“进程保活”。
- APP到后台一点时间后，长连接断开，只能依靠第三方推送，即端外推送。

Android Push分为**通知栏 (Notification)** 和**透传 (Payload)**，两者送达率不同。比如小米的文档中有描述。
> 在一些 Android 系统(如 MIUI)中,受到系统自启动管理设置的限制,应用不能在后台自启动。在这类系统中,如果在发送消息的时候对应的应用没有被启动,透传类消息将不能顺利送达。因此,对于对送达率要求很高的消息,建议尽量采用通知栏提醒的方式推送消息




### 第三方方案
目前第三方PUSH方案：
- 手机厂商
    - 小米
    - 华为
- 第三方平台
    - 友盟
    - 极光
    - 个推
    - 巴云
- BAT平台
    - 阿里云
    - 腾讯信鸽
    - 百度云

#### 各平台特点
 - 厂商：他们的推送服务在他们自己生产的手机上属于系统级别的服务。
 - 专业第三方：“保活”和“互拉”，共享推送通道。
 - BAT大厂：没什么优势，用了信鸽也沾不上微信的光。手机淘宝也使用了友盟推送。
 

比如，在小米手机上，不在系统自启动名单里的App，在手机重启后，App声明的后台Service并不会自动运行。但是，小米推送作为手机系统级服务，仍然是可以收到推送的。

同样，华为推送的技术团队也对外宣称（原话）：
> 华为Push，在华为手机上是系统级别的服务，稳定性等各方面肯定都会好些。

但是，即使是系统级别的推送服务，也不是百分百保证消息送达。这里比较奇葩的是华为推送，下面是他们技术支持给出的描述（原话） 
> 华为手机上：
Emui3.0上，Push广播有很大概率被限制，如： Mate7 3.0版本，荣耀6plus，P7 3.0版本，4X， 4A等。
Emui3.1上，Push广播基本不被限制，但个别型号机型存在问题，如：荣耀5x等。
Emui4.0及以上，Push广播有较高概率被限制，不被限制的机型如：荣耀畅玩4C，荣耀畅玩4X，Mate S，P8 MAX等。
如广播被限制，需要将应用设为开机启动项。所以对于及时性或到达率要求非常高的应用，我们建议应用要考虑替代方案。
后续Push版本，华为将采用新的设计方案，解决被限制的问题，但发布计划待定。

另外，至于限制的问题，其实华为sdk还是能接收到推送消息的，当将消息通过广播发送给应用，如果手机管家查到该应用处于stop状态，那么会拦截该广播的。





#### 各厂商常见问题
> 即使集成了像华为和小米这样的系统级别的推送，也不一定百分百收到消息，即使你在系统设置了自启动，因为有时候你设置了自启动，但是依然不在系统的自启动白名单中。

> 华为系统只有设置了自启动，系统才会考虑拉起应用，系统在接收到推送消息以后，会检查一下自己的系统中的自启动白名单，白名单中放置了所谓的设置过自启动的包名，如果推送消息的包名和不在白名单中，操作系统是不会拉起应用的。（注意，即使你设置了自启动，也不一定在白名单中，你最好看一下系统的日志，把整个推送到达后的系统如何进行处理的日志全部看一下，你就会发现问题在哪里）



## 比较
某平台做的统计，适当参考
![image](http://static.open-open.com/lib/uploadImg/20160711/20160711152842_976.jpg)

### 合作厂商
小米PUSH：


## 测试

### 到达率




## 引用
[国内Top500Android应用分析报告](http://www.open-open.com/lib/view/open1468222124208.html)

[集成Android推送前必看](http://www.jianshu.com/p/017096be88da)

[集成华为推送那些坑](http://www.jianshu.com/p/47a6826f9815)

[微爱cto总结Android 端外推送到底有多烦？](https://juejin.im/post/57a19c012e958a0066715d0c)

[推送“送达率”概念太模糊？友盟带你解读“送达率”背后的那些指标](http://blog.umeng.com/%E5%B7%A5%E7%A8%8B%E6%8A%80%E6%9C%AF/4541.html)

[Android 第三方 Push 推送方案使用调查](https://github.com/android-cn/topics/issues/4#issuecomment-223264673)

[华为官方：Push SDK-客户端常见问题](http://club.huawei.com/thread-10205061-1-1-2851.html)


[华为官方：Push SDK-客户端常见问题](http://club.huawei.com/thread-10205061-1-1-2851.html)


## Set up app in Django
- set the project's setting.py
add 'queen.apps.QueenConfig' into INSTALLED_APPS

- set the project's urls.py
add url patterns. like this:

    urlpatterns = [
    url(r'^queen/', include('queen.urls')),
    url(r'^admin/', admin.site.urls),
    ]


