package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Arrays []int64

func (a Arrays) Len() int           { return len(a) }
func (a Arrays) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a Arrays) Less(i, j int) bool { return a[i] < a[j] }

func ReadNumber(in *bufio.Reader) int64 {
	line, _ := in.ReadString('\n')
	num, _ := strconv.ParseInt(strings.TrimSpace(line[:len(line)-1]), 10, 64)
	return num
}

func ReadArray(in *bufio.Reader) Arrays {
	line, _ := in.ReadString('\n')
	strs := strings.Split(strings.TrimSpace(line[:len(line)-1]), " ")
	nums := make(Arrays, len(strs))
	for i, str := range strs {
		nums[i], _ = strconv.ParseInt(str, 10, 64)
	}
	return nums
}

func main() {
	in := bufio.NewReader(os.Stdin)
	nums1 := ReadArray(in)
	nums2 := ReadArray(in)
	sort.Sort(nums2)
	prev_el := int64(0)
	cuts := 0
	cost := 0
	k := int(nums1[1])
	for i := len(nums2) - 1; i >= 0; i-- {
		if prev_el == 0 {
			prev_el = nums2[i]
		} else {
			if prev_el != nums2[i] {
				diff := int(prev_el - nums2[i])
				for p := 0; p < diff; p++ {
					levCost := len(nums2) - i - 1
					if (cost + levCost) > k {
						cuts++
						cost = levCost
					} else {
						cost += levCost
					}
				}
				prev_el = nums2[i]
			}
		}
	}
	if cost > 0 {
		cuts++
	}
	fmt.Println(cuts)
}
