from src.analysis import InputOutputAnalyzer

def main():
    print("======================================================")
    print(" 2023년 산업연관표(연장표) 기반 경제데이터분석 스크립트 ")
    print("======================================================")
    
    analyzer = InputOutputAnalyzer(data_dir='data')
    
    print("\n[안내] 아래 파일들이 'data' 폴더 내에 정확히 위치해야 코드가 작동합니다:")
    for key, filename in analyzer.files.items():
        print(f" - {filename}")
        
    print("\n분석 스크립트 실행 준비 완료.")
    # 보고서 산출을 위한 데이터 전처리 및 지표 계산 코드를 이 아래에 작성합니다.

if __name__ == '__main__':
    main()
