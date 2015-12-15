/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

package main

import "fmt"
import "os"

func pythagorean_triplet(a int, b int, c int) bool {
	return a * a + b * b == c * c
}

func main() {
	for a := 1; a < 1000; a += 1 {
		for b := 1; b < 1000; b += 1 {
			c := 1000 - a - b
			if pythagorean_triplet(a, b, c) {
				fmt.Println(a*b*c)
				os.Exit(0)
			}
		}
	}
}
