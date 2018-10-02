package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func abs(a int64) int64 {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	line, _ := in.ReadString('\n')
	num, _ := strconv.Atoi(strings.TrimSpace(line[:len(line)-1]))
	nums := make([][3]int64, num)
	for i := 0; i < num; i++ {
		line, _ := in.ReadString('\n')
		strs := strings.Split(strings.TrimSpace(line[:len(line)-1]), " ")
		sub_nums := [3]int64{}
		for i, str := range strs {
			sub_nums[i], _ = strconv.ParseInt(str, 10, 64)
		}
		nums[i] = sub_nums
	}
	for i := 0; i < num; i++ {
		if nums[i][0] > nums[i][2] || nums[i][1] > nums[i][2] {
			fmt.Println(-1)
		} else {
			if (abs(nums[i][0]-nums[i][1]) % 2) == 1 {
				fmt.Println(nums[i][2] - 1)
			} else if (abs(nums[i][2]-min(nums[i][0], nums[i][1])) % 2) == 1 {
				fmt.Println(nums[i][2] - 2)
			} else {
				fmt.Println(nums[i][2])
			}
		}
	}
}
