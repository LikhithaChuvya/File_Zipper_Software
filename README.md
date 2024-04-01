# File_Zipper_Software
This project implements Huffman coding, a compression algorithm assigning variable-length codes to characters based on frequency. It efficiently compresses data by using shorter codes for common characters, reducing storage and transmission needs while maintaining content integrity.

# Huffman Coding Algorithm

Huffman coding is a lossless data compression algorithm. The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters. 
The variable-length codes assigned to input characters are Prefix Codes, means the codes (bit sequences) are assigned in such a way that the code assigned to one character is not the prefix of code assigned to any other character. This is how Huffman Coding makes sure that there is no ambiguity when decoding the generated bitstream. 
Let us understand prefix codes with a counter example. Let there be four characters a, b, c and d, and their corresponding variable length codes be 00, 01, 0 and 1. This coding leads to ambiguity because code assigned to c is the prefix of codes assigned to a and b. If the compressed bit stream is 0001, the de-compressed output may be “cccd” or “ccb” or “acd” or “ab”.

# Features:

Huffman tree construction from input data.
Generation of Huffman codes for each character.
Compression of input data using generated Huffman codes.
Decompression of compressed data to retrieve the original data.

# Usage:

Clone the repository to your local machine.
Place your input file(s) in the same directory as the script.
Run the script to compress the input file(s).
The compressed output will be stored in separate file(s).

# File Structure:

huffman_coding.py: Main script implementing Huffman coding algorithm.
input.txt: Example input file for compression.
compressed.bin: Compressed output file.
output_log.txt: Log file containing details of compression process.

# Contributing:

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.

# License:

This project is licensed under the MIT License.
