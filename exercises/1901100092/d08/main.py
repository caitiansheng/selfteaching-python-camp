text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

美丽总比丑陋好
显式比隐式好
简单总比复杂好
复杂总比复杂好
平的比嵌套的好
稀疏总比密集好
可读性
特殊情况还不足以打破规则
虽然实用性胜过纯洁性
错误不应该悄无声息地过去
除非显式地沉默
面对敏锐，拒绝猜测的诱惑
应该有一种——而且最好只有一种——显而易见的方法来做到这一点
不过，除非你是荷兰人，否则这种方式一开始可能并不明显
现在总比不做好
虽然从来没有比“现在”更好
如果实现很难解释，这是一个坏主意
如果实现很容易解释，这可能是一个好主意
名称空间是一个很棒的主意——让我们做更多这样的事情
'''

from mymodule import stats_word
text=1                  #验证参数检查功能是否生效
try:
    print(stats_word.stats_text(text))
except ValueError:
    print('stats_text参数应为字符串类型')