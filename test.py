def say_hello(name):
    str = "Hello," + name
    print(str)

if __name__ == '__main__':
    name = input("What's your name ?: ")
    #sayhelloを呼び出すためにはどうしたらよいでしょう？
    say_hello(name)
