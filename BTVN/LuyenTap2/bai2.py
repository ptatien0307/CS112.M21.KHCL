def troll(jobs):
    selected_jobs = 1
    prev_job = 0
    for i in range(1, len(jobs)):
        if (jobs[i][0] >= jobs[prev_job][1]):
            prev_job = i
            selected_jobs += 1
    return selected_jobs

def main():
    n = int(input())
    jobs = []
    for _ in range(n):
        jobs.append(list(map(int, input().split())))
    print(troll(sorted(jobs, key = itemgetter(1))))

if __name__ == '__main__':
    from operator import itemgetter
    main()