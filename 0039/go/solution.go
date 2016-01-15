/*
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
*/

// Brute force :(
// Some optimizations

package main

import "fmt"

func main() {
	best_count := 0
	best_p := 0
	for p := 10; p <= 1000; p += 2 {
		count := 0
		for a := 1; a < p - 1; a += 1 {
			for b := a; b + a < p; b += 1 {
				c := p - a - b
				if a*a + b*b == c*c {
					count += 1
				}
			}
		}
		if count > best_count {
			best_count = count
			best_p = p
		}
	}
	fmt.Println(best_p)
}
