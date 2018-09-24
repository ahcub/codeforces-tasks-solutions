package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func ReadNumber() (int) {
	in := bufio.NewReader(os.Stdin)
	line, _ := in.ReadString('\n')
	num, _ := strconv.Atoi(strings.TrimSpace(line[:len(line)-1]))
	return num
}

func ReadArray() ([]int) {
	in := bufio.NewReader(os.Stdin)
	line, _ := in.ReadString('\n')

	strs := strings.Split(strings.TrimSpace(line[:len(line)-1]), " ")
	nums := make([]int, len(strs))
	for i, str := range strs {
		nums[i], _ = strconv.Atoi(str)
	}
	return nums
}

func main() {
	n := ReadNumber()
	fmt.Println(n)
	nums := ReadArray()
	fmt.Println(nums)
}
