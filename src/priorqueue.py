class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	# Periksa apakah queue kosong
	def isEmpty(self):
		return len(self.queue) == 0

	# Untuk memasukkan data ke queue
	def push(self, data):
		self.queue.insert(0, data)

	# Untuk mengeluarkan elemen dari queue
	def delete(self):
		try:
			min = 0
			for i in range(len(self.queue)):
				if self.queue[i].cost + self.queue[i].depth < self.queue[min].cost + self.queue[min].depth:
					min = i
			item = self.queue[min]
			del self.queue[min]
			return item
		except IndexError:
			print()
			exit()

