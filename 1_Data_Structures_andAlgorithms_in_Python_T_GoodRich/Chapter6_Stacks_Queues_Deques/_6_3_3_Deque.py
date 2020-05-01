class Deque(object):
	DEFAULT_CAPICITY = 5
	def __init__(self):
		self._size = 0
		self._front = 0
		self._data = [None]*Deque.DEFAULT_CAPICITY
		
	def __len__(self):
		return self._size

	def add_first(self, e):
		if self._size == len(self._data):
			self.resize(len(self._data))
		if not self.is_empty():
			# if the front index already has an element, advance the front leftward
			self._front = ( self._front - 1 ) % len(self._data)
		self._data[self._front] = e
		self._size += 1

	def add_last(self, e):
		if self._size == len(self._data):
			self.resize(len(self._data)*2)
		back = ( self._front + self._size ) % len(self._data)
		self._data[back] = e
		self._size += 1

	def delete_first(self):
		assert not self.is_empty(), 'Deque Empty'
		e = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front + 1) % len(self._data)
		self._size -= 1
		if 0 < self._size < len(self._data)//4:
			self.resize(len(self._data)//2)
		return e

	def delete_last(self):
		assert not self.is_empty(), 'Deque Empty'
		back = (self._front + self._size - 1) % len(self._data)
		e = self._data[back]
		self._data[back] = None
		self._size -= 1
		if 0 < self._size < len(self._data)//4:
			self.resize(len(self._data)//2)
		return e

	def first(self):
		assert not self.is_empty(), 'Deque Empty'
		return self._data[self._front]

	def last(self):
		assert not self.is_empty(), 'Deque Empty'
		back = (self._front + self._size - 1) % len(self._data)
		return self._data[back]

	def is_empty(self):
		return self._size == 0

	def resize(self, old_size):
		old_data = self._data
		temp_front = self._front
		self._data = [None]*old_size
		for i in range(self._size):
			self._data[i] = old_data[temp_front]
			temp_front = (temp_front + 1) % len(old_data)
		self._front = 0

	def display(self):
		print(self._data)


def main():
	print('main')
	D = Deque()
	D.add_first(1)
	D.display()
	D.add_first(2)
	D.display()
	D.add_first(3)
	D.display()
	D.add_first(4)
	D.display()
	D.add_first(5)
	D.display()
	D.add_last(6)
	D.display()
	D.add_last(7)
	D.display()
	D.add_last(8)
	D.display()
	print(len(D))


	print(D.delete_first())
	D.display()
	print(D.delete_first())
	D.display()
	print(D.delete_first())
	D.display()
	print(D.delete_last())
	D.display()
	print(D.delete_last())
	D.display()
	print(D.delete_last())
	D.display()
	print(D.delete_last())
	D.display()
	print(D.delete_last())
	D.display()


main()