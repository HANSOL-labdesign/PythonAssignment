import os
import pickle

filename = 'score.bin'

def input_scores():
    scores = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        scores.append(n)
        i += 1
    return scores

def get_average(scores):
    if scores:
        return sum(scores) / len(scores)
    else:
        return 0

def show_scores(scores):
    print('[점수 출력]')
    print('개인점수:', *scores)
    print(f'평균: {get_average(scores):.1f}')
    print()

def save_scores(scores):
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)

def load_scores():
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    else:
        return None

def main():
    scores = load_scores()
    if scores is not None:
        print('[파일 읽기]')
        print()
        show_scores(scores)
    else:
        print('[점수 입력]')
        scores = input_scores()
        show_scores(scores)
        save_scores(scores)

if __name__ == '__main__':
    main()



