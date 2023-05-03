# ⚙ Smart Queue Library

Smart Queue is a Python library that provides a simple queue of synchronous tasks. This library is built on top of Python's built-in `queue` module and is useful when you want to perform multiple tasks that can cause race conditions or I/O conflicts.

## Installation

Clone this repository and run setup:
```bash
python3 setup.py install
```

### Usage

Library provides a `SmartQueue` class, which is the main object for using this library.

```python
from smart_queue import SmartQueue, Task

def my_task():
  print("hello world")

queue = SmartQueue()
queue.push(Task(my_task))
queue.push(Task(my_task))
queue.start()
```

In the example above, we create a `SmartQueue` instance and push two `Task` objects to it. Then, we start the queue so that it begins processing the tasks one by one.

You can push multiple tasks to the queue, and they will be executed in the order they were received (FIFO).

### Tasks

A `Task` is simply a callable function that should be executed by the `SmartQueue`. You can pass any function to a `Task`, and it will be executed when the `Task` is processed by the queue.

```python
from smart_queue import SmartQueue, Task

def my_task():
  print("Heavy computation going on...")
  return 2 + 2

queue = SmartQueue()
queue.push(Task(my_task))
queue.start()
```

In the example above, we create a `Task` with a function that performs heavy computation and returns a result. When the `Task` is processed by the queue, it executes the `my_task` function.

### Callbacks

You can specify a callback function to be executed once the task is complete. You need to pass the callback function as a parameter to the `Task` object.

```python
from smart_queue import SmartQueue, Task

def my_task():
  print("Heavy computation going on...")
  return 2 + 2

def my_callback(result):
  print(f"Task complete! Result: {result}")

queue = SmartQueue()
queue.push(Task(my_task, callback=my_callback))
queue.start()
```

In the example above, we specify a callback function to be called once the task is complete. The `result` argument to the callback function is the return value of the task.

## License

This library is licensed under the MIT License. See the LICENSE file for more information."