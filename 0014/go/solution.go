/*
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

package main

import "fmt"

func collatz_length(n int) int {
	length := 1
	for n != 1 {
		for n % 2 == 1 {
			n = 3 * n + 1
			length += 1
		}
		for n % 2 == 0 {
			n /= 2
			length += 1
		}
	}
	return length
}

func main() {
	/* partial dynamic programming */
	/* this could be even more memoized, but I won't for now */
	var lengths [1000000]int
	value, max := 0, 0
	for i := 1; i < 1000000; i += 1 {
		if lengths[i] != 0 {
			continue
		}
		length := collatz_length(i)
		lengths[i] = length
		if length > max {
			max = length
			value = i
		}
	}
	if value == 0 {
		fmt.Println("An error occured.")
	}
	fmt.Println(value)
}
