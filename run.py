###### 變數
a = 0 #整數
b = 'b' #字串
c = True #布林
d = False #布林
e = "e" #字串
f = 3.14 #浮點數
g = a #賦值

###### 方法
def 方法1():
  return "Hi"
print(方法1) #輸出Hi

def 方法2(文字):
  return 文字
print(方法二("測試")) #輸出測試

def 加法(a,b):
  c = a+b
  return c
print(加法(1,2)) #輸出3

###### 常見方法
a = input('請輸入A:')
b = input("請輸入B:")
print(int(a)+int(b)) #印出加法
print(加法(int(a),int(b))) #跟上面一樣
