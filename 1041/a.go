package main

import (
	"fmt"
	"io"
)

func main() {
	var n int
	fmt.Scanln(&n)
	a := make([]int, n)
	fmt.Fscanln(io.St, &a)
	fmt.Println(a)
}
