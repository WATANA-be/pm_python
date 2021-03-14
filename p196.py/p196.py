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
