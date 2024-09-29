# Job Array (Job Name, Deadline, Profit)
arr = [['a', 4, 50], 
       ['b', 3, 10],
       ['c', 1, 45],
       ['d', 4, 90],
       ['e', 1, 40],
       ['f', 1, 5]]

# Maximum number of time slots (find the maximum deadline in the array)
max_deadline = max(job[1] for job in arr)

# Sort jobs by profit in descending order
arr.sort(key=lambda x: x[2], reverse=True)

# Time slots (initially all are free, represented by 0)
time_slots = [0] * max_deadline  # For deadlines 1, 2, 3, 4...

# To keep track of the selected jobs
selected_jobs = [None] * max_deadline

# Total profit variable
total_profit = 0

# Iterate over each job and try to place it in the latest available slot before its deadline
for job in arr:
    job_name, deadline, profit = job
    
    # Find a free slot for this job (starting from the last possible slot before the deadline)
    for t in range(min(deadline - 1, max_deadline - 1), -1, -1):
        if time_slots[t] == 0:  # If the slot is free
            time_slots[t] = 1  # Mark this slot as filled
            selected_jobs[t] = job_name  # Assign the job to this slot
            total_profit += profit  # Add the job's profit to the total profit
            break  # Job has been assigned, so exit the loop

# Output the selected jobs and the total profit
print("Selected jobs:", selected_jobs)
print(f"Total profit: {total_profit}")
