# pcr_robot
公主连结休闲公会战机器人v1.0
## 现有功能
### 1.主动命令
#### (1) 记录出刀
格式：/记录 玩家名称 boss编号 伤害数值  
* 玩家名称: 需要在成员列表中  
* boss编号: 1-5的整数  
* 伤害数值: 就...整数数字  

不符合格式会显示记录失败信息  
PS:0-5点的记录会存储在昨天的记录中  
### 2.自动功能
#### (1) 提醒出刀/报刀
每日定时(目前为23:30),at当日未记录满3刀以上的成员