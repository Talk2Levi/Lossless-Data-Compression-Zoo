# Lossless-Data-Compression-Zoo [![HitCount](http://hits.dwyl.io/LeviIsAwesome/https://github.com/LeviIsAwesome/lossless-data-compression-zoo.svg)](http://hits.dwyl.io/LeviIsAwesome/https://github.com/LeviIsAwesome/lossless-data-compression-zoo)
This repository contains a number of different lossless text compression algorithms implemented in Python.

## Main Contributors
The project is for the final case study of a __Graduated Level Course: Online Algorithm__, and the original main contributors were (names in alphabetical order):

| [<img src="https://avatars2.githubusercontent.com/u/37234961?s=400&v=4" width="100px;"/><br /><sub><b>Levi Guo</b></sub>](https://github.com/LeviIsAwesome)  | [<img src="https://avatars3.githubusercontent.com/u/28665314?s=400&v=4" width="100px;"/><br /><sub><b>Ehidiamen Osarhemen</b></sub>](https://github.com/MingoLi)  | [<img src="https://avatars1.githubusercontent.com/u/10003885?s=400&v=4" width="100px;"/><br /><sub><b>Ye Yuan</b></sub>](https://github.com/LongWinter)  |  
|---|---|---|


## Dataset
The dataset was trasformed using Burrows-Wheeler text Transform (BWT) before passing to the data compression algorithm which offers a better input locality and time-and-space performances. ([link](https://github.com/nicolaprezza/BWTIL/tree/master/tools/dB-hash) for the BWT library)

## Algorithm 
* **[Move to Front(MTF)](https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/mtf.py)**: Moves the requested item to the front.

* **[Timestamp(TS)](https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/timestamp.py)**: Inserts an accessed item x in front of the first item y (from the front of the list) that precedes x in the list and was accessed at most once since the last access to x. If there is no such item y or x is accessed for the first time, Timestamp does not move the item.

* **[Move by Bit(MBB)](https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/move_by_bit.py)**: Each item has a bit associated with it. At the beginning, all bits are 0. After an access to an item x, MBB moves it to the front if the bit of x is 1; otherwise, it keeps x at its position. In addition, after each access, the bit of the accessed item is flipped.                                   
![](algorithm%20demo/mbb.gif)           

* **[Move to Front Random(MTFR)](https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/mtf_random.py)**:
A variant of MTF. Instead of moving the item to the first position (index 0) in the list, it moves it to the index based on a randomly generated number which is in the range of [0, current index]. The seed that is used by the random generator is encoded in the file in order to decompress. In this project, we use 1 as the random seed.                        
![](algorithm%20demo/random.gif)

* **[Move to Front Reverse](https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/mtf_reverse.py)**: Upon accessing an item at index i, reverse the ordering of the first i items in the list (the accessed item will be moved to the front)                        
![](algorithm%20demo/reverse.gif)                  

* **[Move to Front Reverse 2](https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/mtf_reverse2.py)**: The improved version of move to front reverse. This improved algorithm reversing all the items in front of the one being accessed, it only reverses a small chunk of items. e.g. if the chunk size is defined as 10 and the index being accessed is 90, then the algorithm reverses the item in range[80, 90] (The chunk size was default set to be 10 in the algorithm).       

## List Update Problem
A classical algorithm in the context of Self-adjusting data structures. Given a set of items in a list where the cost of accessing an item is proportional to its distance from the head of the list.

## Data Compression
One important application of list update is in data compression. Given a data sequence, we want to do lossless compression, i.e. we should be able to recover the exact text from the compressed one.

## Algorithm Performance
The best performed data compression algorithm for the most of testing input is the simplest one which MTF in red, i.e. the algorithm with the lowest competitive ratio, and a few runner-up algorithms are in brown. 
![](https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/algorithm%20demo/algorithm%20running%20persormance.png)
