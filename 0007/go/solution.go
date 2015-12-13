/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

// Brute force :(

package main

import "fmt"

func special_prime(n int) bool {
	if n % 2 == 0 {
		return false
	}
	for i := 3; i * i <= n; i += 2 {
		if n % i == 0 {
			return false
		}
	}
	return true
}

func main() {
	i := 3
	for count := 1; count < 10001; i += 2 {
		if (special_prime(i)) {
			count += 1
		}
	}
	fmt.Println(i - 2)
}
