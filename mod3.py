from main import main1
from mod1 import test1
from mod2 import test2

func1 = main1()
if func1.multitab == "tab1":
    test1(func1.var1)
elif func1.multitab == "tab2":
    test2(func1.var2)
