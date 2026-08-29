from bisect import bisect_right


def max_profit_job_scheduling(startTime, endTime, profit):
    jobs = list(zip(startTime, endTime, profit))

    # Sort jobs by ending time
    jobs.sort(key=lambda x: x[1])

    n = len(jobs)

    # dp[i] = maximum profit using first i jobs
    dp = [0] * (n + 1)

    end_times = [job[1] for job in jobs]

    for i in range(1, n + 1):
        start, end, p = jobs[i - 1]

        # Find number of jobs that end <= current start
        j = bisect_right(end_times, start, 0, i - 1)

        # Option 1: skip current job
        skip = dp[i - 1]

        # Option 2: take current job
        take = p + dp[j]

        dp[i] = max(skip, take)

    return dp[n]


# Test Case 1
startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]

print("Maximum profit:", max_profit_job_scheduling(
    startTime, endTime, profit
))

# Test Case 2
startTime = [1, 2, 3, 4, 6]
endTime = [3, 5, 10, 6, 9]
profit = [20, 20, 100, 70, 60]

print("Maximum profit:", max_profit_job_scheduling(
    startTime, endTime, profit
))
