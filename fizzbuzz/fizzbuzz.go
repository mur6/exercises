// Run:
// $ go run fizzbuzz.go

package main

import (
	"fmt"
	"strconv"
)

const N = 100

func fizzbuzz() []string {
	result := make([]string, N)
	for i := 0; i < N; i++ {
		j := i + 1
		switch {
		case j%15 == 0:
			result[i] = "FizzBuzz!"
		case j%3 == 0:
			result[i] = "Fizz"
		case j%5 == 0:
			result[i] = "Buzz"
		default:
			result[i] = strconv.Itoa(j)
		}
	}
	return result
}

func main() {
	for _, s := range fizzbuzz() {
		fmt.Println(s)
	}
}
