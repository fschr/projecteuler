/*
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
*/

package main

import "fmt"

func pf(n int) bool {
	dpf := 0
	for n % 2 == 0 {
		n /= 2
		dpf = 1
	}
	for i := 3; n != 1; i += 2 {
		if n % i == 0 {
			n /= i
			dpf += 1
			if dpf > 4 {
				return false
			}
			for n % i == 0 {
				n /= i
			}
		}
	}
	return dpf == 4
}

func main() {
	for i := 50000; true; {
		if pf(i) {
			if pf(i + 1) {
				if pf(i + 2) {
					if pf(i + 3) {
						fmt.Println(i)
						break
					} else {
						i += 4
					}
				} else {
					i += 3
				}
			} else {
				i += 2
			}
		} else {
			i += 1
		}
	}
}
