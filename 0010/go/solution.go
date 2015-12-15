/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

package main

import "fmt"

/* Brute force :( */

func prime(n int) bool {
	if n < 2 {
		return false
	} else if n == 2 {
		return true
	} else if n % 2 == 0 {
		return false
	}
	for i := 3; i * i <= n; i += 1 {
		if n % i == 0 {
			return false
		}
	}
	return true
}

func main() {
	sum := 2
	for i := 3; i < 2000000; i += 2 {
		if prime(i) {
			sum += i
		}
	}
	fmt.Println(sum)
}
