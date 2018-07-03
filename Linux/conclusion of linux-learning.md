# linux学习-知识图谱

[TOC]

## 1. 内部培训学习内容

### 1.1 linux常用命令

**命令格式**： command options arguments

#### a. 目录

**部分也可以操作文件** 

| 命令  | 解释                                   | 示例         |
| ----- | -------------------------------------- | ------------ |
| ls    | 显示指定工作目录下之内容               | ls -Al /home |
| dir   | 同ls                                   |              |
| cd    | 变换工作目录                           |              |
| pwd   | 显示用户当前工作路径                   |              |
| mkdir | 创建新的目录                           |              |
| rmdir | 删除已建立的目录                       |              |
| rm    | 删除文档及目录                         |              |
| touch | 创建一个空白文件或改变已有文件的时间戳 |              |
| cp    | 复制文件或目录                         |              |
| mv    | 移动文件或目录（重命名）               |              |
| ln    | 建立链接                               |              |
| chmod | 修改文件或目录的权限                   |              |
| chown | 修改文件或目录所属的用户               |              |
| chgrp | 修改文件或目录所属的工作组             |              |

#### b. 查看文件

| 命令 | 解释 | 示例 |
| ---- | ---- | ---- |
| more |      |      |
| less |      |      |
| head |      |      |
| tail |      |      |
| cat  |      |      |
|      |      |      |

#### c. 查找

| 命令 | 解释 | 示例 |
| ---- | ---- | ---- |
| find |      |      |
| locate |      |      |
| grep |      |      |
|      |      |      |


#### d. 用户操作

| 命令 | 解释 | 示例 |
| ---- | ---- | ---- |
| who |      |      |
| finger |      |      |
| su |      |      |
| sudo |      |      |
| passwd |      |      |
| login |      |      |
| logout |      |      |
|      |      |      |

#### e. 系统相关

| 命令 | 解释 | 示例 |
| ---- | ---- | ---- |
| date |      |      |
| shutdown |      |      |
| reboot |      |      |
| ftp |      |      |
| telnet |      |      |
| mail |      |      |
| free |      |      |
| du   |      |      |
| df   |      |      |
| top |      |      |

#### f. 压缩和解压缩

| 命令    | 解释 | 示例 |
| ------- | ---- | ---- |
| tar     |      |      |
| rpm     |      |      |
| gzip    |      |      |
| gunzip  |      |      |
| bzip2   |      |      |
| bunzip2 |      |      |



#### g. 其他

| 命令    | 解释 | 示例 |
| ------- | ---- | ---- |
| mount   |      |      |
| unmount |      |      |
| ssh     |      |      |
| man     |      |      |
| clear   |      |      |
| scp     |      |      |

### 1.2 Find命令使用详解

**find命令格式**： find pathname -options [-print -exec -ok ...] 

#### a. find命令的参数

pathname

-print

-exec

-ok

#### b. find命令选项

-name

-type

-perm

-prune

-depth

-user

-group

-mtime -n +n

#### d. 使用exec或ok来执行shell命令

任何形式的命令都可以在-exec选项中使用： ls -l, rm -f, grep, ...
在shell中用任何方式删除文件之前，如rm， mv, 首先应当查看相应的文件 。使用-exec选项的安全模式 -ok, 它会对每个匹配到的文件进行操作之前提示你

```shell
find ./ -type f -exec ls -l {} \;
find ./ -name "*.md" -mtime +3 -ok rm {} \; 
```
#### e. xargs

xargs - build and execute command lines from standard input 

find 命令把匹配到的文件传递给 xargs 命令，而 xargs 命令每次只获取一部分文件而不是全部，不像-exec 选项那样是。这样它可以先处理最先获取的一部分文件，然后是下一批，并如此继续下去。

### 1.3 Vi编辑器

Vi编辑器是所以Unix及Linux系统下标准的编辑器

vi没有菜单，只有命令

VI环境设定      set nu, set nonu,  set autoindent, set noautoindent

#### a. vi的三种基本工作模式

- 命令模式（command mode)
- 插入模式（insert mode)
- 末行模式（last line mode)

#### b. vi 的进入与退出

vi +n filename

:wq

ZZ

#### c. 插入模式

- a, A, 
- i, I
- o, O



- ESC

#### d. 末行模式

- :    命令
- /    查找
- ?    查找

#### e. 搜索和替换

/子串

?子串

n, N

子串搜索与替换

:10,20s/old/new 将第10行至第20行资料的'old'改成'new'
:%s/old/new/g 将编辑缓冲区中所有的'old'改成'new'

#### f. 命令模式下，文本的编辑/删除/复制

$: 行尾

0: 行首

n: 数量

删除: (字符)x, dh,  (单词和行)dw, db, dd, d$, d0, <n>dd ,
    (文本块) d),  d(,  d},   d{

替换字符： 在需要替换的字符处， r+<new>

复制：yy, nyy, (剪切)dd, ndd
粘贴： p

#### g. vi 常用快捷键

方向快捷键：
          k
h                   I
           j

0, $
gg, G
nG
:n

### 1.4 linux下shell编程

Shell是一种具备特殊功能的程序， 它是介于使用者和 UNIX/Linux 操作系统之核心程序（kernel）间的一个接口

n为了对用户屏蔽内核的复杂性，也为了保护内核以免用户误操作造成损害，在内核的周围建了一个外壳(shell)。用户向shell提出请求，shell解释并将请求传给内核。 

nshell的另一个重要特性是它自身就是一个解释型的程序设计语言，支持绝大多数在高级语言中能见到的程序元素，如函数、变量、数组和程序控制结构。shell编程语言简单易学，任何在提示符中能键入的命令都能放到一个可执行的shell程序中。 

n本质上，shell 脚本是命令行命令简单的组合到一个文件里面。Shell基本上是一个命令解释器，类似于DOS下的command.com。它接收用户命令，然后调用相应的应用程序。

#### a. 开始写脚本

```shell
#!/bin/sh
#ShowHello.sh
#To show hello to somebody
echo -n "Enter Your Name:"
read NAME
echo "Hello, ${NAME}!"
```

#### b. 权限管理

rwx

u, g, o, a

#### c. 变量

变量一般用大写字母表示，使用变量时，前面加$

本地变量：用户自定义的变量。

环境变量：用于所有用户变量，用于用户进程前，必须用export命令导出。

位置变量：$0(脚本名)，$1-$9:脚本参数。

特定变量：脚本运行时的一些相关信息。



$#, $*, $$, $!, $@, $-, $?

#### d. 条件测试

格式： [ expression ]    方括号两边各有一个空格，示例如下

0表示成功，其他表示失败

```shell
[ "10" -eq "12" ]
```

文件状态测试

字符串测试

数值测试

#### e. 结构控制

选择结构

- if 语句： 

```shell
  if [ grade > 90 ]
      then
          echo "优秀"
  elif [ grade > 80 ]
      then
          echo "良好"
  else
      echo "一般"
  fi
```


- case语句:  

```shell
  case 值 in
    模式1）
        echo "This is one"
        ;;
    模式2）
        echo "This is two"
        ;;
    *)
        echo "This is default"
  esca
```

 循环结构

- for循环

```shell
for 变量名 in 列表
do 
    expressions
done
```

- until 循环

```shell
until 条件
do
    expressions
done
```

- while

```shell
while 条件
do
    expression
done
```

#### f. 函数

所有函数在使用前必须定义
调用函数仅使用其函数名即可，要传给函数的变量跟在函数后面
函数里面定义的变量以下划线开始
```shell
#!/bin/sh
#funTest
#to test the function
DATE=`date`
Hello()
{
  echo “Hello,today is $DATE”
}
Hello
```

### 1.5 makefile教程

详细信息可参考 [makefile 使用总结](https://www.cnblogs.com/wang_yb/p/3990952.html) 

#### a. 开发过程

编辑 -> 编译 -> 链接 -> 运行 -> 调试

#### b. gcc使用

预处理：gcc -E main.c -o main.i

编译: gcc -S main.i -o main.s

汇编: gcc -c main.s -o main.o

链接: gcc -O main.o -o main

gcc main.c -o main

#### c. 语法

target: prerequiries
	command
	command

前缀

- "-": 忽略命令错误，继续执行
-  "@":不输出命令

伪目标： all, clean

#### d. 变量

自动化变量

- $< 当前规则的第一个prerequisite
- $@ 当前规则的target
- $^ 当前规则的所有prerequisites

环境变量： $(PWD), env

规则变量：target: CFLAG= -c -O3 -Wall

#### e. 规则

隐含规则

```makefile
hello: hello.o
	gcc -o hello -g -Wall hello.o
	
# 输出为：
gcc -c -o hello.o hello.c
gcc -o hello -g -Wall hello.o
```

模式规则 %.o: %.c

```makefile
%.o: %.c
	gcc -c $< -o $@
```

目标和依赖中的%值相同

后缀规则

```makefile
.cpp.o:
	$(GCC) $(CFLAG) -o $@ $< 
```

#### f. 小结

```makefile
cc = gcc
prom = calc
deps = $(shell find ./ -name "*.h")
src = $(shell find ./ -name "*.c")
obj = $(src:%.c=%.o) 

$(prom): $(obj)
    $(cc) -o $(prom) $(obj)

%.o: %.c $(deps)
    $(cc) -c $< -o $@

clean:
    rm -rf $(obj) $(prom)
```

### 1.6 linux实战-2小时玩转iptables

详细可查看博客 [朱双印个人日志](http://www.zsythink.net/archives/1199) 

#### a. 框架图

PREROUTING, FORWARD, POSTROUTING, INPUT, OUTPUT 以及路由转发的关系

#### b. 链和表

链：PREROUTING, FORWARD, POSTROUTING, INPUT, OUTPUT

表： raw, mangle, nat, filter

#### c. 语法

iptables  [-t 要操作的表] 
       <操作命令>
       [要操作的链]
       [规则号码]
       [匹配条件]
       [-j 匹配到以后的动作] 

#### d. 命令

操作命令 -A,  -I, -D, -R, -P, -F

查看命令 -[vnx]L

#### e. 匹配条件

流入、流出接口  -i, -o

来源、目的地址  -s, -d

协议类型             -p

来源、目的端口  --sport,  --dport

示例：

1、端口匹配
-p udp--dport53 匹配网络中目的端口是 53 的 UDP 协议数据包

2、地址匹配 
-s 10.1.0.0/24 -d 172.17.0.0/16 匹配来自 10.1.0.0/24 去往 172.17.0.0/16 的所有数据包

3、端口和地址联合匹配 
-s 192.168.0.1 -d www.abc.com-p tcp--dport80 匹配来自 192.168.0.1，去往 www.abc.com 的 80 端口的 TCP 协议数据包

#### f. 动作（处理方式）

ACCEPT

DROP

SNAT

DNAT

MASQUERADE

#### g. 附加模块

- 按包状态匹配（ state） -m state --state 状态 
- 按来源 MAC 匹配（mac）  -m mac--mac-source MAC 
- 按包速率匹配（ limit）  -m limit --limit 匹配速率 [--burst 缓冲数量] 
- 多端口匹配（ multiport）-m multiport<--sports|--dports|--ports> 端口1[,端口2,..,端口n]  必须与-p一起使用

### 1.7 练习题




```

```