/*
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
*/

package main

import "fmt"

func main() {
	/* The answer is just 40 choose 20 */
	var answer uint64 = 1024
	for i := uint64(39); i > 20; i -= 2 {
		answer *= i
	}
	for i := uint64(10); i > 0; i -= 1 {
		answer /= i
	}
	fmt.Println(answer)
}
