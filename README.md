stock-trading
=============

Emulate stock trading

Collaborated with @davinwong

## Choice of data structures

I chose to encapsulate bids and their operations inside the `class Bids`. I used python's heap to represent the actual bids. Since python doesn't offer native support for max-heap, I stored all bid values as negatives and used the min-heap. The time space complexity for building a max-heap is `O(N)` if processed sequentially from a list and `O(nlog(n))` if inserted one at a time while maintaining sort order; the space complexity of building a max-heap is `O(N)`. The time and space complexity for insertion and deletions are `O(log(N))`. Finally, the time and space complexicity of extracting k elements is `O(klog(n))` and `O(k)` respectively.

I chose max-heaps because its suitable for maintaining mostly sorted data sets. It has a low build cost and allows us to get top k elements in only `O(klog(n))`, contrasting it to quick-sorting a list with `O(n^2)`. To reduce latency of processing and outputing top k bids, which is absolutely essential to high speed trading applications, it makes sense to use max-heaps over lists or other data structures.

## Done
* Load max-heap bids with history
* Output `top n k`
* Respond to input

## In progress
* Start bid streams on separate threads

## To do
* Synchronize bid stream bids to main thread bids object
* Test suite

## Resources used
* http://stackoverflow.com/
* http://docs.python.org/
