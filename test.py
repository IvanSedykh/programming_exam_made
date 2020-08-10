import numpy as np

x = int(input())
# x = 1


for _ in range(x):
    N, K = list(map(int, input().split()))
    # N, K = 8, 2

    sections = np.array(
        list(map(int, input().split()))
    )

    # sections = np.array([2, 3, 4, 5, -30, 6, -1, 2])
    scores = np.zeros(shape=(N, N), dtype='int')
    for start in range(N):
        for stop in range(N):
            if stop >= start:
                if K >= start and K <= stop and K != -1:
                    score = 0
                else:
                    score = np.sum(sections[start:stop + 1])
            else:
                if K < start and K > stop or K == -1:
                    score = np.sum(sections) - np.sum(sections[stop + 1:start])
                else:
                    score = 0
            scores[start, stop] = score

    # print(scores)
    print(scores.max())
