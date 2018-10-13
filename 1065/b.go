package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func ReadNumber(in *bufio.Reader) int64 {
	line, _ := in.ReadString('\n')
	num, _ := strconv.ParseInt(strings.TrimSpace(line[:len(line)-1]), 10, 64)
	return num
}

func ReadArray(in *bufio.Reader) []int64 {
	line, _ := in.ReadString('\n')
	strs := strings.Split(strings.TrimSpace(line[:len(line)-1]), " ")
	nums := make([]int64, len(strs))
	for i, str := range strs {
		nums[i], _ = strconv.ParseInt(str, 10, 64)
	}
	return nums
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func main() {
	in := bufio.NewReader(os.Stdin)
	nums := ReadArray(in)
	if nums[1] == 0 {
		fmt.Printf("%d %d", nums[0], nums[0])
	} else {
		max_val := nums[0] - int64(math.Ceil((1.0+math.Sqrt(float64(1+8*nums[1])))/2))
		fmt.Printf("%d %d", max(nums[0]-nums[1]*2, 0), max_val)
	}
}
