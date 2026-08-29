def minimum_time(jobs, k):
    jobs.sort(reverse=True)

    workers = [0] * k
    answer = sum(jobs)

    def backtrack(index):
        nonlocal answer

        if index == len(jobs):
            answer = min(answer, max(workers))
            return

        job = jobs[index]

        for i in range(k):

            # Pruning: assigning this job already exceeds answer
            if workers[i] + job >= answer:
                continue

            # Avoid assigning to workers with same current workload
            if workers[i] in workers[:i]:
                continue

            workers[i] += job

            # Current maximum workload
            current_max = max(workers)

            if current_max < answer:
                backtrack(index + 1)

            workers[i] -= job

            # If this worker was empty, no need to try
            # other empty workers.
            if workers[i] == 0:
                break

    backtrack(0)
    return answer


# Test Case 1
jobs = [3, 2, 3]
k = 3
print("Minimum maximum working time:", minimum_time(jobs, k))

# Test Case 2
jobs = [1, 2, 4, 7, 8]
k = 2
print("Minimum maximum working time:", minimum_time(jobs, k))
