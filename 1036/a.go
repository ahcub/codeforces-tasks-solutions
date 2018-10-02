package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

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
	nums := ReadArray()
	res := nums[1] / nums[0]
	if (nums[1] % nums[0]) != 0 {
		res += 1
	}
	fmt.Println(res)
}
