import pandas as pd
import numpy as np
import os

class InputOutputAnalyzer:
    def __init__(self, data_dir='data'):
        # 경기대 경제학과 과제 보고서용 데이터 로더
        # 사용자가 제공한 6개의 한국은행 엑셀 파일명 원본 그대로 매핑
        self.files = {
            '기본부문': '(표)(2023연장)투입산출표_생산자가격_기본부문_2.xlsx',
            '대분류': '(표)(2023연장)투입산출표_생산자가격_통합대분류_2.xlsx',
            '중분류': '(표)(2023연장)투입산출표_생산자가격_통합중분류_2.xlsx',
            '소분류': '(표)(2023연장)투입산출표_생산자가격_통합소분류_2.xlsx',
            '상품분류': '(표)상품분류_2.xlsx',
            '연장표총괄': '2023년 산업연관표(연장표)_2.xlsx'
        }
        self.data_dir = data_dir
        self.dataframes = {}

    def load_data(self, category='대분류'):
        '''지정된 분류의 산업연관표 엑셀 데이터를 로드합니다.'''
        filepath = os.path.join(self.data_dir, self.files[category])
        if os.path.exists(filepath):
            print(f"[{category}] 데이터를 로드합니다: {self.files[category]}")
            # 한국은행 산업연관표 양식에 맞추어 헤더와 인덱스를 스킵하는 로직이 필요할 수 있습니다.
            self.dataframes[category] = pd.read_excel(filepath)
            return self.dataframes[category]
        else:
            raise FileNotFoundError(f"파일 누락: {filepath}. 'data' 폴더 안에 해당 엑셀 파일이 정확한 이름으로 들어있는지 확인해주세요.")

    def calculate_leontief_inverse(self, A_matrix):
        '''
        레온티에프 역행렬 (I - A)^-1 계산 함수
        경제데이터분석 보고서 작성 시 생산유발계수 도출에 사용됩니다.
        '''
        I = np.identity(len(A_matrix))
        I_A = I - A_matrix
        L_matrix = np.linalg.inv(I_A)
        return L_matrix

if __name__ == '__main__':
    analyzer = InputOutputAnalyzer()
    print("데이터 분석 모듈 초기화 완료.")
