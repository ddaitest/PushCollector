# result

Test cases
1. APP正常打开情况
2. APP切到后台
3. APP被划杀
4. 手机清内存
5. 锁屏
6. 解锁后，停留在HOME
7. 启动APP，停留5分钟。
8. 锁屏

|Device|OS|Android|
|-|-|-|
|华为ZUK Z2			|ZUI 2.5.334		|7.0|
|华为  mt7-cl00		|emui4.0			|6.0|
|华为 MT1-U06 (71)	|emotion1.5		|4.1.2|
|华为 MT1-U07 (72)	|emotion1.5		|4.1.2|
|华为 mate9			|eui5.0			|7.0|
|小米3				|miui8.2.3.0		|4.4.4|
|红米 HM2LTE-CU		|MIUI 8.1		|4.4.4|
|SONY L39H			|14.4.A.0.108	|4.4.4|
|三星 Galaxy S4		|				|4.4.2|
|三星 note3 lite4g	|				|4.3|
|1+ A0001			|ColorOS 1,2,0	|4.3|
|coolpad 5952		|				|4.3|
|vivo x9i			|funtouch OS 3.0	|6.0.1|

## app 在前台 (Notification)


|Device|HUAWEI|MI|GETUI|UMENG|XG|
|-|-|-|-|-|-|
|华为ZUK Z2			|x  |   |n |  |  |
|华为  mt7-cl00		|n  |n  |n | n|  |
|华为 MT1-U06 (71)	|x  |n  |n | n| n|
|华为 MT1-U07 (72)	|x  |n  |n | n| n|
|华为 mate9			|n  |n  |n | n|  |
|小米3				|x  |n  |n | n|  |
|红米 HM2LTE-CU		|x  |n  |  | n| n|
|SONY L39H			|x  |n  |n | n|  |
|三星 Galaxy S4		|x  |n  |n | n|  |
|三星 note3 lite4g	|x  |n  |n | n|  |
|1+ A0001			|x  |n  |n | n|  |
|coolpad 5952		|x  |n  |n | n|  |
|vivo x9i			|x  |n  |n | n| n|

## APP 在前台 （Payload）

|Device|HUAWEI|MI|GETUI|UMENG|XG|
|-|-|-|-|-|-|
|华为ZUK Z2			|x |p  |p | p|  p|
|华为  mt7-cl00		|p |p  |p | p|   |
|华为 MT1-U06 (71)	|x |p  |p | p|  p|
|华为 MT1-U07 (72)	|x |p  |p | p|  p|
|华为 mate9			|p |p  |p | p|   |
|小米3				|x |p  |p | p|   |
|红米 HM2LTE-CU		|x |p  |  | p|   |
|SONY L39H			|x |p  |p | p|   |
|三星 Galaxy S4		|x |p  |p | p|  p|
|三星 note3 lite4g	|x |p  |p | p|   |
|1+ A0001			|x |p  |p | p|  p|
|coolpad 5952		|x |p  |p | p|  p|
|vivo x9i			|x |p  |p | p|  p|

## APP 切到后台 （Notification）

|Device|HUAWEI|MI|GETUI|UMENG|XG|
|-|-|-|-|-|-|
|华为ZUK Z2			|  |n |n |n  |   |
|华为  mt7-cl00		|n |n |n |n  |   |
|华为 MT1-U06 (71)	|  |n |n |n  | n |
|华为 MT1-U07 (72)	|  |n |n |n  |   |
|华为 mate9			|n |n |n |n  | n |
|小米3				|  |n |  |   |   |
|红米 HM2LTE-CU		|  |n |  |n  | n |
|SONY L39H			|  |n |n |n  | n |
|三星 Galaxy S4		|  |n |n |n  | n |
|三星 note3 lite4g	|  |n |n |n  | n |
|1+ A0001			|  |n |n |n  |   |
|coolpad 5952		|  |n |n |n  |   |
|vivo x9i			|  |n |n |n  | n |

## APP 切到后台 （Payload）

|Device|HUAWEI|MI|GETUI|UMENG|XG|
|-|-|-|-|-|-|
|华为ZUK Z2			|  |p |p | p | p |
|华为  mt7-cl00		|p |p |p | p |   |
|华为 MT1-U06 (71)	|  |p |p | p |   |
|华为 MT1-U07 (72)	|  |p |p | p | p |
|华为 mate9			|p |p |p | p | p |
|小米3				|  |p |  | p |   |
|红米 HM2LTE-CU		|  |p |  | p | p |
|SONY L39H			|  |p |p | p | p |
|三星 Galaxy S4		|  |p |p | p |   |
|三星 note3 lite4g	|  |p |p | p | p |
|1+ A0001			|  |p |p | p | p |
|coolpad 5952		|  |p |p | p |   |
|vivo x9i			|  |p |p | p | p |

## APP 被杀

|Device|HUAWEI|MI|GETUI|UMENG|XG|
|-|-|-|-|-|-|
|华为ZUK Z2			|  |  |  |  |  |
|华为  mt7-cl00		|  |n |  |n |  |
|华为 MT1-U06 (71)	|  |n |n |n |n |
|华为 MT1-U07 (72)	|  |n |n |n |  |
|华为 mate9			|n |n |  |n |n |
|小米3				|  |n |  |  |  |
|红米 HM2LTE-CU		|  |n |n |n |  |
|SONY L39H			|  |n |n |n |  |
|三星 Galaxy S4		|  |n |n |n |  |
|三星 note3 lite4g	|  |n |n |n |  |
|1+ A0001			|  |n |n |n |n |
|coolpad 5952		|  |  |  |n |  |
|vivo x9i			|  |  |  |  |  |

##  手机清内存

|Device|HUAWEI|MI|GETUI|UMENG|XG|
|-|-|-|-|-|-|
|华为ZUK Z2			|  |  |  |  |  |
|华为  mt7-cl00		|n |  |  |  |  |
|华为 MT1-U06 (71)	|  |n |n |n |  |
|华为 MT1-U07 (72)	|  |n |n |n |n |
|华为 mate9			|n |  |  |n |  |
|小米3				|  |n |  |  |  |
|红米 HM2LTE-CU		|  |n |  |  |  |
|SONY L39H			|  |  |  |  |  |
|三星 Galaxy S4		|  |n |n |n |  |
|三星 note3 lite4g	|  |n |n |n |n |
|1+ A0001			|  |  |n |n |  |
|coolpad 5952		|  |  |n |n |  |
|vivo x9i			|  |  |  |  |  |

## 锁屏

|Device|HUAWEI|MI|GETUI|UMENG|XG|
|-|-|-|-|-|-|
|华为ZUK Z2			|  |  |  |  |  |
|华为  mt7-cl00		|n |  |  |  |  |
|华为 MT1-U06 (71)	|  |n |n |n |  |
|华为 MT1-U07 (72)	|  |n |n |n |  |
|华为 mate9			|n |  |  |  |  |
|小米3				|  |n |  |  |  |
|红米 HM2LTE-CU		|  |n |  |  |  |
|SONY L39H			|  |  |n |n |  |
|三星 Galaxy S4		|  |n |n |n |  |
|三星 note3 lite4g	|  |n |n |n |n |
|1+ A0001			|  |  |n |n |  |
|coolpad 5952		|  |  |  |n |n |
|vivo x9i			|  |  |  |  |  |

## APP 在前台时候锁屏

|Device|HUAWEI|MI|GETUI|UMENG|XG|
|-|-|-|-|-|-|
|华为ZUK Z2			|  |n |n |n |n |
|华为  mt7-cl00		|n |n |n |n |  |
|华为 MT1-U06 (71)	|  |n |n |n |  |
|华为 MT1-U07 (72)	|  |n |n |n |n |
|华为 mate9			|  |  |  |  |  |
|小米3				|  |n |n |n |n |
|红米 HM2LTE-CU		|  |n |n |n |n |
|SONY L39H			|  |n |n |n |  |
|三星 Galaxy S4		|  |n |n |n |n |
|三星 note3 lite4g	|  |n |n |n |  |
|1+ A0001			|  |n |n |n |  |
|coolpad 5952		|  |n |n |n |n |
|vivo x9i			|  |  |  |  |  |