package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func ReadNumber() int64 {
	in := bufio.NewReader(os.Stdin)
	line, _ := in.ReadString('\n')
	num, _ := strconv.ParseInt(strings.TrimSpace(line[:len(line)-1]), 10, 64)
	return num
}

func ReadArray() []int64 {
	in := bufio.NewReader(os.Stdin)
	line, _ := in.ReadString('\n')

	strs := strings.Split(strings.TrimSpace(line[:len(line)-1]), " ")
	nums := make([]int64, len(strs))
	for i, str := range strs {
		nums[i], _ = strconv.ParseInt(str, 10, 64)
	}
	return nums
}

func main() {
	n := ReadNumber()
	fmt.Println(n)
	nums := ReadArray()
	fmt.Println(nums)
}
