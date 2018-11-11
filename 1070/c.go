package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Arrays [][4]int

func (a Arrays) Len() int           { return len(a) }
func (a Arrays) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a Arrays) Less(i, j int) bool { return a[i][3] < a[j][3] }

func main() {
	in := bufio.NewReader(os.Stdin)
	line, _ := in.ReadString('\n')
	strs := strings.Split(strings.TrimSpace(line[:len(line)-1]), " ")
	base := [3]int{}
	for i, str := range strs {
		base[i], _ = strconv.Atoi(str)
	}
	tarifs := make(Arrays, base[2])
	dotsToSplitMap := make(map[int]bool)
	for i := 0; i < base[2]; i++ {
		line, _ := in.ReadString('\n')
		strs := strings.Split(strings.TrimSpace(line[:len(line)-1]), " ")
		for j, str := range strs {
			tarifs[i][j], _ = strconv.Atoi(str)
		}
		tarifs[i][1] += 1
		dotsToSplitMap[tarifs[i][0]] = true
		dotsToSplitMap[tarifs[i][1]] = true
	}
	sort.Sort(tarifs)
	dotsToSplit := make([]int, 0, len(dotsToSplitMap))
	for k := range dotsToSplitMap {
		dotsToSplit = append(dotsToSplit, k)
	}
	sort.Ints(dotsToSplit)
	dateRangesTarifPlans := make(map[[2]int][][2]int)
	for _, tarif := range tarifs {
		lef := findIndex(dotsToSplit, tarif[0])
		rig := findIndex(dotsToSplit, tarif[1])
		for i := lef + 1; i < rig+1; i++ {
			k := [2]int{dotsToSplit[i-1], dotsToSplit[i]}
			dateRangesTarifPlans[k] = append(dateRangesTarifPlans[k], [2]int{tarif[2], tarif[3]})
		}
	}
	totalPrice := 0
	for k := range dateRangesTarifPlans {
		cores := base[1]
		daysDiff := k[1] - k[0]
		for _, v := range dateRangesTarifPlans[k] {
			if v[0] > cores {
				totalPrice += daysDiff * cores * v[1]
				break
			} else {
				totalPrice += daysDiff * v[0] * v[1]
				cores -= v[0]
			}
		}
	}
	fmt.Println(totalPrice)
}

func findIndex(listToCheck []int, index int) int {
	left := 0
	right := len(listToCheck) - 1
	for {
		if left == right {
			return left
		}
		mid := left + ((right - left) / 2)
		if listToCheck[mid] <= index && index <= listToCheck[mid] {
			return mid
		}
		if listToCheck[mid] > index {
			right = mid
		} else {
			left = mid + 1
		}
	}
}
