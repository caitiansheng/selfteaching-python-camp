7.20 day 1 学习任务：使用github进行协作
第一天的内容要求是基本的安装。由于提前看过《 自学是门手艺 》，就已经照着书在电脑上安装了jupterlab和注册了github，可是当我照着自学准备要求进行时才发现安装有许多的问题，由于怕出差错我不得不重新进行安装，花费了许久的时间。

7.20 day 2 学习任务：安装配置环境变量
安装Anaconda和vscode花费了一定的时间，因为刚接触vscode较困难的方面是在vscode中配置python环境，我查询了许多网上资料和参考资料才了解应该怎么配置。我主要是根据资料把环境更改为Python 3.7.3-bit(‘base’:conda),语言环境我没有进行更改，比较能适应英语环境。

7.22 day3  学习任务：了解python以及使用vscode编写简单计算器
今天已经开始编写任务我可以说是一头雾水。初尝试编写计算器对与我新手而言一点都不简单。我只有不停的翻阅李笑来老师的《自学是门手艺》和去google上搜索有效信息，自己不停的尝试不同的代码编写最后才完成简单计算机的编写。
输入，输出Input()Print()
处理多种情况 if…elif….elif…else

7.23 day4学习任务 :使用 for…in 打印九九乘法表
今天的学习刚好对应李笑来老师的《自学是门手艺》，书里面刚好给出了如何使用for…in，while，偶数的·运行代码，这对编写代码非常有帮助。
循环While continue break pass

7.24-7.25 day5 
任务开始繁重和费力，一共有三个任务需要完成，我花了两天的时间进行这项学习。在代码运行期间一直出差错不是我想要的结果不停的修改，有时候感到无力可是还是坚持自己研究，当得到我想要的结果时我觉得非常有意义。
进行排序 sorted（）
大小写翻转swapcase()

7.26-27 day6
我开始放慢了学习的脚步，我开始花2天的时间完成一项自学内容。今天的内容与day5的相似，可是当我需要使用def定义函数的时候,之后的代码的输入前面都需要tab空格，同时学习了运用创建空白文档整理单词，使用split除去字符
中文汉字与英文单词统计出现次数的方式的相同，只不过中文汉字不需要去除一些符号。Print（）前不需要tab空格。

7.28-7.29 day7 
自学内容需要添加一个新函数，合并输出day6的内容。因为day6的时候学习了如何定义新的函数，所以重新添加一个新函数合并没有很困难。可是运行代码时还是出现了许多问题。比如中文汉字并没有按个数排列，只能对之前的代码进行修改，添加了中文字符的范围代码。在使用from…import去调用文件的时候，mymodule里的文件一直运行不了,最后就只采用了import….

7.30-8.1 day8
学习内容为python中的异常处理主要是针对ValueError。我对这个内容也是不太了解看了很多遍参考资料。
Try：
……
Except ValueError:
……

8.2 day9
关于使用counter去完善排序功能，把每个定义函数后面都加上了一个count，并且返还到collections.Counter most-common([n])这个函数上，return…..读取tang300文件我尝试了好几种方法，一直读取不正确,最后根据参考资料上的代码
打开本地文件with open(‘’)as f
	      read_data=f.read()
  	 f.close

8.4 day10
自学内容比较复杂的是要通过三方中文分词库统计词频。安装jieba时出现问题，mac系统需要在pip install jieba之后添加链接才能安装成功。

8,5 day11
Day11的内容比较有趣是把整理的文章以邮件的形式发送。成功安装了yagmail，pyquery和requests。从微信上提取文章,对文章进行整理。代码运行无误可是邮件一直发送不成功，询问了教练才知道密码是需要授权码。
from pyquery import pyQuery;
document=PyQuery(response.text);
content=document(‘#js_content’).text()

8.7 day12
Day12依然是实战练习，通过微信发送消息。由于安装wxpy受到了限制导致后面运行不成功，不过还是在运行时自动出现了二维码觉得很神奇。
from wxpy impot*
bot=Bot()
my_friend = bot.friends
@bot.register(my_friend,sharing)
转化为str类型 str()
添加新对象append()

8.13 day13
最后一天的内容参考参考资料可以输出图片，可是最后一天的内容并不简单花费了很多时间去研究如何生成图片。根据参考资料给出了如何制作图画以及图画的信息，同时需要加入了前几天作业的内容。

在自学的过程中我收获颇多，我能静下心来自己研究和学习我不会的东西。刚开始的时候我做不完就不休息，可以一整天坐在电脑面前不休息不停的尝试，甚至导致我晚上睡觉都还在想代码。之后我放慢了脚步，想不清楚就慢慢来，多看书查阅有效的资料参考大家的作业思路视频等，使得我最后几天的任务都完成得较快。我很享受研究的过程，虽然有时很辛苦很没头绪，可是当得到想要的结果时格外的开心有成就感。感谢教练还有助教一路的陪伴，指出了存在的问题并且及时给予我帮助。
