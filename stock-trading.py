import sys
import heapq
import time
import threading

EXIT_FLAG = 1

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
		print N, self.number_of_bids
		if N <= self.number_of_bids:
			with open(filename, 'w') as fs_output:
				for bid in self.getTopNBids(N):
					fs_output.write(str(bid))
					fs_output.write(' ')

				fs_output.write('\n')

	def loadHistory(self, filename):
		with open(filename, 'r') as fs_hist:

			self.number_of_bids = int(fs_hist.readline())
			
			for bid in fs_hist:
				# Storing as -1 since default heap implementation is min-heap
				heapq.heappush(self.sorted_bids, -1 * int(bid.rstrip('\n'))) 

class BidStream(threading.Thread):
	def __init__(self, bs):
		threading.Thread.__init__(self)
		self.bs = bs
	def run(self):
		with open(self.bs, 'r') as bs_fs:
			while True:
				if EXIT_FLAG == 0:
					return True

				where = bs_fs.tell()
				line = bs_fs.readline()
				if not line:
					time.sleep(1)
					bs_fs.seek(where)
				else:
					bid_value = line.strip() # already has newline
					print bid_value
					print bids.sorted_bids
					# Add bid to bids max-heap
					bids.addBid(int(bid_value))

def stock_trading(history, inpt, output, bs1_name=None, bs2_name=None, bs3_name=None, bs4_name=None):
	global bids
	global EXIT_FLAG

	bids = Bids()
	bids.loadHistory(history)

	# Set up bidstream threads
	bs1 = BidStream(bs1_name)

	# Start bitstream threads
	bs1.start()

	# Tail -f feature from stackoverflow
	with open(inpt, 'r') as input_fs:
		while EXIT_FLAG:
			where = input_fs.tell()
			line = input_fs.readline()
			if not line:
				time.sleep(1)
				input_fs.seek(where)
			else:
				command = line.strip() # already has newline
				if command == "end":
					EXIT_FLAG = 0
				elif len(command.split(' ')) == 3: # assuming top command with pos integers
					print command
					cmd, top, number_of_bids = command.split(' ')
					top = int(top)

					print bids.sorted_bids

					if bids.number_of_bids > number_of_bids:
						bids.outputTopNBids(output, top)

	print "Exiting program!"

def main(args):
	if len(args) < 8:
		print "Missing args!"
	elif len(args) > 8:
		print "Too many args!"
	else:
		name, hist, inpt, outpt, bs1, bs2, bs3, bs4 = args

	stock_trading(hist, inpt, outpt, bs1, bs2, bs3, bs4)

if __name__ == '__main__':
	main(sys.argv)