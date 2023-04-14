def minimumWaitingTime(queries):
    sorted_queries = sorted(queries)
    total = 0
    for idx,duration in enumerate(sorted_queries):
        queries_left = len(sorted_queries) - (idx+1)
        total += queries_left*duration
    return total


queries =  [3, 2, 1, 2, 6]
minimumWaitingTime = minimumWaitingTime(queries)
print(minimumWaitingTime)