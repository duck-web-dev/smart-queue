from typing import Callable
from threading import Event, Thread
from queue import Queue as _default_queue

class Task:
	def __init__(self, task: Callable, callback: Callable = lambda: None, *args, **kwargs):
		self.task = task
		self.callback = callback
		self.callback_args = args
		self.callback_kwargs = kwargs
	def run(self, callback_event: Event = None, ):
		result = self.task()
		if callback_event: callback_event.set()
		self.callback(result, *self.callback_args, **self.callback_kwargs)


class SmartQueueException(Exception):
	pass

class SmartQueue:
	def __init__(self):
		self.queue = _default_queue()
		self.newitem_event = Event()
		self.should_stop = False
		self.stop_event = Event()
		self.__mainloop_running = False

	@property
	def size(self):
		return self.queue.qsize()
	
	def push(self, task: Task):
		if not isinstance(task, Task): raise TypeError("Must be a Task instance")
		self.queue.put(task)
		self.newitem_event.set()
		
	def start(self, ignore_errors: bool = False):
		''' Starts loop of handling tasks, stop by using `SmartQueue.stop()` method. Use `ignore_errors` to ignore failed tasks.'''
		if self.__mainloop_running: raise SmartQueueException('Loop is already running.')
		self.should_stop = False
		self._mainloop(ignore_errors)
	def stop(self, block: bool = True):
		''' Stop loop of handling tasks. If `block` argument is True, wait for loop to exit. '''
		self.should_stop = True
		self.stop_event.clear()
		if block: self.stop_event.wait()
	def _mainloop(self, i: bool):
		Thread(target=self.mainloop, args=(i, )).start()
	def mainloop(self, ignore_errors: bool):
		self.__mainloop_running = True
		if self.should_stop:
			self.__mainloop_running = False
			self.stop_event.set()
			return
		if self.size <= 0:
			self.newitem_event.clear()
			self.newitem_event.wait(3)
			self._mainloop(ignore_errors)
		else:
			task: Task = self.queue.get()
			try:
				task.run()
			except Exception as e:
				if ignore_errors:
					print('Error occured while running task:', e)
				else:
					self.__mainloop_running = False
					self.stop_event.set()
					raise SmartQueueException('Error occured while running task:', e)
			self._mainloop(ignore_errors)
