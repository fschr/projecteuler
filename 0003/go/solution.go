/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

package main

import "fmt"

func main() {
     var n = 600851475143
     var gpf int
     for i := 3; i <= n; i += 2 {
     	 for n % i == 0 {
	     n = n / i
	     gpf = i
	 }
     }
     fmt.Println(gpf)
}