import pandas as pd
import argparse
import matplotlib.pyplot as plt

# 커맨드 라인 인자 파싱을 위한 설정
parser = argparse.ArgumentParser(description="Draw histograms for three CSV files.")
parser.add_argument('file1', type=str, help='Path to the first CSV file')
parser.add_argument('file2', type=str, help='Path to the second CSV file')
parser.add_argument('file3', type=str, help='Path to the third CSV file')
parser.add_argument('--bins', type=int, default=10, help='Number of bins for the histogram')  # bins 인자 추가

# 인자 파싱
args = parser.parse_args()

# 각 CSV 파일에서 'execution_time' 데이터를 읽음
df1 = pd.read_csv(args.file1)
df2 = pd.read_csv(args.file2)
df3 = pd.read_csv(args.file3)

# 'execution_time' 히스토그램 그리기
plt.figure(figsize=(15, 5))  # 히스토그램을 가로로 나열하기 위한 figure 크기 설정

# 첫 번째 파일 히스토그램
plt.subplot(1, 3, 1)
plt.hist(df1['execution_time'], bins=args.bins, color='skyblue', edgecolor='black')
plt.title(f"Histogram of {args.file1}")
plt.xlabel('Execution Time')
plt.ylabel('Frequency')

# 두 번째 파일 히스토그램
plt.subplot(1, 3, 2)
plt.hist(df2['execution_time'], bins=args.bins, color='salmon', edgecolor='black')
plt.title(f"Histogram of {args.file2}")
plt.xlabel('Execution Time')
plt.ylabel('Frequency')

# 세 번째 파일 히스토그램
plt.subplot(1, 3, 3)
plt.hist(df3['execution_time'], bins=args.bins, color='lightgreen', edgecolor='black')
plt.title(f"Histogram of {args.file3}")
plt.xlabel('Execution Time')
plt.ylabel('Frequency')

# 그래프 간격을 자동 조정하여 겹치지 않게 함
plt.tight_layout()

# 히스토그램을 PNG 이미지로 저장
plt.savefig('histograms.png', format='png')

# 히스토그램 표시
# plt.show()
