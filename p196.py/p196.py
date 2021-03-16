class MyCoach:
    '''鬼コーチクラス
    '''
    def __init__(self,max):
        '''
        初期化メソッド
        self:インスタンスの参照情報
        max:繰り返しの回数
        '''
        self.max = max#インスタンス変数maxをmaxで初期化
        self.count = 0

    def teach(self):
        '''
        熱血指導メソッド
        self:インスタンスの参照情報
        '''
        if self.count < self.max:
            print('もっと強く！')
        else:
            print('オッケーだ！')
        self.count += 1

class MyCoach2:
    '''
    鬼コーチクラス
    '''
    count = 0
    max = 5
    def teach(self):
        if self.__class__.count<self.__class__.max:
            #countがmax未満の時の処理
            print('もっと強く！')
        else:
            #countがmaxに達したら以下を実行
            print('オッケーだ！！！')
        self.__class__.count += 1

my1 = MyCoach2()
for i in range(3):
    print('スマッシュ')
    my1.teach()

my2 = MyCoach2()
for i in range(3):
    print('ライジング')
    my2.teach()