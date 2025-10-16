class SayHello:
    # 2.プログラムの初期化メソッド
    def __init__(self, target="World"):
        self.target = target

    def say(self):
        print(f"Hello, {self.target}!!")

# 1.プログラムのスタート地点
if __name__ == "__main__":
    app = SayHello()
    app.say()
    app = SayHello("Someone")
    app.say()