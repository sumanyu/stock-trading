import sys
import heapq
import time

class Bids:
	number_of_bids = 0
	sorted_bids = []

	def addBid(self, bid):
		heapq.heappush(self.sorted_bids, bid)
		self.number_of_bids += 1

	def addBids(self, list_of_bids):
		for bid in list_of_bids:
			addBid(bid)

	def getTopNBids(self, N):
		if N <= self.number_of_bids:
			# Convert from negative to positive
			return [-1*x for x in heapq.nsmallest(N, self.sorted_bids)]

	def outputTopNBids(self, filename, N):
		if N <= self.number_of_bids:
			with open(filename, 'w') as fs_output:
				for bid in self.getTopNBids(N):
					fs_output.write(str(bid))
					fs_output.write(' ')

				fs_output.write('\n')

	def loadHistory(self, filename):
		with open(filename, 'r') as fs_hist:

			self.number_of_bids = fs_hist.readline()
			
			for bid in fs_hist:
				# Storing as -1 since default heap implementation is min-heap
				heapq.heappush(self.sorted_bids, -1 * int(bid.rstrip('\n'))) 

def stock_trading(history, inpt, output, bidstream1=None, bidstream2=None, bidstream3=None, bidstream4=None):
	bids = Bids()
	bids.loadHistory(history)

	with open(inpt) as input_fs:
		while True:
			where = input_fs.tell()
			line = input_fs.readline()
			if not line:
				time.sleep(1)
				input_fs.seek(where)
			else:
				print line # already has newline

	# print bids.getTopNBids(3)
	# bids.outputTopNBids(output, 3)

def main(args):
	if len(args) < 8:
		print "Missing args!"
	elif len(args) > 8:
		print "Too many args!"
	else:
		name, hist, inpt, outpt, bidstream1, bidstream2, bidstream3, bidstream4 = args

	stock_trading(hist, inpt, outpt, bidstream1, bidstream2, bidstream3, bidstream4)

if __name__ == '__main__':
	main(sys.argv)