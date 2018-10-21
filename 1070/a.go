package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	nums := ReadArray(in)
	dis := make([][]*[3]int, nums[0])
	for i, _ := range dis {
		dis[i] = make([]*[3]int, nums[1]+1)
	}
	dis[0][0] = &[3]int{0, 0, 0}
	queue := make([][2]int, 0)
	queue = append(queue, [2]int{0, 0})
	var el [2]int
	for len(queue) > 0 {
		el = queue[0]
		queue = queue[1:]
		for i := 0; i < 10; i++ {
			xx := (10*el[0] + i) % nums[0]
			yy := el[1] + i
			if yy > nums[1] || dis[xx][yy] != nil {
				continue
			} else {
				dis[xx][yy] = &[3]int{el[0], el[1], i}
				queue = append(queue, [2]int{xx, yy})
			}
		}
	}
	if dis[0][nums[1]] == nil {
		fmt.Println("-1")
	} else {
		out(0, nums[1], &dis)
	}

}

func ReadArray(in *bufio.Reader) []int {
	line, _ := in.ReadString('\n')
	strs := strings.Split(strings.TrimSpace(line[:len(line)-1]), " ")
	nums := make([]int, len(strs))
	for i, str := range strs {
		nums[i], _ = strconv.Atoi(str)
	}
	return nums
}

func out(x, y int, d *[][]*[3]int) {
	if x == 0 && y == 0 {
		return
	} else {
		out((*d)[x][y][0], (*d)[x][y][1], d)
		fmt.Print((*d)[x][y][2])
	}
}
