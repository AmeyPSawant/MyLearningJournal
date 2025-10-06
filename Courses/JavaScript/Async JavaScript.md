# Async JavaScript

## Difference between Sync and Async

Lets assume four tasks at hand-  
Task 1 - 5 sec  
Task 2 - 2 sec  
Task 3 - 15 sec  
Task 4 - 1 sec

If using **async** the maximum completion time would be **15 sec** as all the processes have started simultaneously.  
Whereas in sync mode, the total completion time would be **5 + 2 + 15 + 1 = 23 sec**.

## Async code hints in JS

- setTimeout
- setInterval
- promises
- fetch
- axios
- XMLHttpRequest
