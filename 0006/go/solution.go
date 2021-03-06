/*
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

/* The square of the sum of the first n natural numbers is n(n+1)n/2 */
/* The sum of the squares of the first n natural numbers is n(n+1)(2n + 1)/6 */

package main

import "fmt"

func square(n int) int {
	return n * n;
}

func main() {
	fmt.Println(square(100*(100 + 1) / 2) - 100*(100 + 1)*(2 * 100 + 1) / 6)
}
