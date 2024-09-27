import heapq
 
# 10, 11, 12, 13, 14
# 0   1    2   3  4
def printJobScheduling(arr):
    n = len(arr)
 
    # arr[i][0] = job_id, arr[i][1] = deadline, arr[i][2] = profit
 
    # sorting the array on the basis of their deadlines
    arr.sort(key=lambda x: x[1])
 
    # initialize the result array, maxHeap and total_profit
    result = []
    maxHeap = []
    total_profit = 0  # Total profit starts at 0
 
    # starting the iteration from the end
    for i in range(n - 1, -1, -1):
 
        # calculate slots between two deadlines
        if i == 0:
            slots_available = arr[i][1]
        else:
            slots_available = arr[i][1] - arr[i - 1][1]
 
        # include the profit of job(as priority), deadline
        # and job_id in maxHeap
        # note we push negative value in maxHeap to convert
        # min heap to max heap in python
        heapq.heappush(maxHeap, (-arr[i][2], arr[i][1], arr[i][0]))
 
        while slots_available and maxHeap:
 
            # get the job with max_profit
            profit, deadline, job_id = heapq.heappop(maxHeap)
 
            # reduce the slots
            slots_available -= 1
 
            # include the job in the result array
            result.append([job_id, deadline])
            
            # add the profit of the job to the total profit
            total_profit += -profit  # Don't forget to negate back to positive
 
    # jobs included might be shuffled
    # sort the result array by their deadlines
    result.sort(key=lambda x: x[1])
 
    for job in result:
        print(job[0], end=" ")
    print()
    
    # print the total profit
    print(f"Total profit: {total_profit}")
 
# Driver's Code
if __name__ == '__main__':
    arr = [['a', 4, 50],  # Job Array
           ['b', 3, 10],
           ['c', 1, 45],
           ['d', 4, 90],
           ['e', 1, 40],
           ['f', 1, 5]]
 
    print("Following is the maximum profit sequence of jobs:")
 
    # Function Call
    printJobScheduling(arr)

