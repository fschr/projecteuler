/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

package main

import "fmt"
import "os"

func palindromify(x int, y int, z int) int {
     return (1e5 * z + 1e4 * y + 1e3 * x +
     	    1e2 * x + 1e1 * y + z);
}

/* Brute force :( */
func main() {
     for one := 9; one >= 1; one -= 1 {
     	 for two := 9; two >= 0; two -= 1 {
	     for three := 9; three >= 0; three -= 1 {
	         var num = palindromify(three, two, one)
	         for a := 100; a < 1000; a += 1 {
	     	     for b := 100; b < 1000; b += 1 {
		         if a * b == num {
			     fmt.Println(num)
			     os.Exit(0)
			 }
		     }
	         }
	     }
	 }
     }
}