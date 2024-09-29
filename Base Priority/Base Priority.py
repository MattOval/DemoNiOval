import threading
import queue
import time

# A lock to ensure only one thread executes at a time
lock = threading.Lock()

# A function that simulates a task with a delay (sleep) after it is completed
def task(name, priority):
    with lock:  # Ensures that only one task runs at a time
        print(f"Task {name} with priority {priority} started.")
        time.sleep(1)  # Simulate work for 1 second
        print(f"Task {name} completed.")
        time.sleep(2)  # Sleep for 2 seconds after the task is completed

# Worker function to process tasks from the priority queue
def worker(q):
    while True:
        # Get the next task from the queue (priority, name)
        priority, name = q.get()
        if name is None:  # If a 'None' signal is received, break the loop to stop the worker
            break
        task(name, priority)  # Execute the task
        q.task_done()  # Mark the task as done in the queue

# Create a priority queue
priority_queue = queue.PriorityQueue()

# Create and start worker threads
num_worker_threads = 3  # We want 3 threads to run tasks in parallel
threads = []
for _ in range(num_worker_threads):
    t = threading.Thread(target=worker, args=(priority_queue,))  # Create a thread and assign it the worker function
    t.start()  # Start the thread
    threads.append(t)  # Keep track of the threads in the list

# Adding tasks to the priority queue (lower number means higher priority)
priority_queue.put((2, 'Task 1'))  # Task 1 has priority 2 (medium)
priority_queue.put((1, 'Task 2'))  # Task 2 has priority 1 (highest priority)
priority_queue.put((3, 'Task 3'))  # Task 3 has priority 3 (lowest priority)

# Wait for all tasks to be processed
priority_queue.join()

# Send stop signal to the worker threads
for _ in range(num_worker_threads):
    priority_queue.put((0, None))  # Send a 'None' signal to stop each worker thread

# Wait for all worker threads to finish
for t in threads:
    t.join()

print("All tasks completed.")
