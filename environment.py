class Environment:
    PRICE_IDX = 4 # 종가의 위치

    def __init__(self, chart_data=None):# 차트 데이터 저장해주기
        self.chart_data = chart_data
        self.observation = None
        self.idx = -1

    def reset(self):
        self.observation = None
        self.idx = -1

    def observe(self):
        if len(self.chart_data) > self.idx + 1:
            self.idx += 1
            self.observation = self.chart_data.iloc[self.idx]# 데이터에서 위치요소 가져오는 DataFrame함수
            return self.observation
        return None

    def get_price(self):# 종가 가져와 반환
        if self.observation is not None:
            return self.observation[self.PRICE_IDX]
        return None

    def set_chart_data(self, chart_data):
        self.chart_data = chart_data