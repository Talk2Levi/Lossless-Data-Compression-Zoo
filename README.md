# lossless_compression_zoo
This repository contains a number of different lossless text compression algorithms implemented in Python.

## Main Contributors:
The project is for the final case study of a __Graduated Level Course: Online Algorithm__, and the original main contributors were (names in alphabetical order):
**[Levi Guo](https://github.com/LeviIsAwesome), [Minghao Li](https://github.com/MingoLi), [Ye Yuan](https://github.com/LongWinter).**

## Dataset
The dataset was trasformed using Burrows-Wheeler text Transform (BWT) before passing to the data compression algorithm which offers a better input structure and time-and-space performances. ([link](https://github.com/nicolaprezza/BWTIL/tree/master/tools/dB-hash) for the BWT library)

## Algorithm 
 **[Move to Front(MTF)](https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/mtf.py)**:

Moves the requested item to the front.

**[Timestamp(TS)]**(
https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/timestamp.py):
inserts an accessed item x in front of the first item y (from the front of the
list) that precedes x in the list and was accessed at most once since the last access to x. If
there is no such item y or x is accessed for the first time, Timestamp does not move the item.

 **[Move to Front Random(MTFR)](https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/mtf_random.py)**:
A variant of MTF. Instead of moving the item to the first
position (index 0) in the list, it moves it to the index based on a randomly generated number
which is in the range of [0, current index]. The seed that is used by the random generator is
encoded in the file in order to decompress. In this project, we use 1 as the random seed.
* **Move by Bit** see at:               
https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/move_by_bit.py

* **Move to Front Reverse** see at:             
https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/mtf_reverse.py
* **Move to Front Reverse Improved Version** see at:             
https://github.com/LeviIsAwesome/lossless_compression_zoo/blob/master/mtf_reverse2.py

## Presentation
https://docs.google.com/presentation/d/18E2skjwf0Gcw-_0YD8Fz-Ma0GJLFb3v6rymqCCbUZT8/edit?usp=sharing
