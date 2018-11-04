package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Arrays [][2]uint64

func (a Arrays) Len() int           { return len(a) }
func (a Arrays) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a Arrays) Less(i, j int) bool { return a[i][0] < a[j][0] }

var whiteList, blackList Arrays
var ipRanges []string
var ranges map[uint64]string
var multipliers [4]uint64

func main() {
	multipliers = [4]uint64{16777216, 65536, 256, 1}
	ranges = map[uint64]string{
		1: "32", 2: "31", 4: "30", 8: "29", 16: "28",
		32: "27", 64: "26", 128: "25", 256: "24", 512: "23",
		1024: "22", 2048: "21", 4096: "20", 8192: "19",
		16384: "18", 32768: "17", 65536: "16", 131072: "15",
		262144: "14", 524288: "13", 1048576: "12", 2097152: "11",
		4194304: "10", 8388608: "9", 16777216: "8", 33554432: "7",
		67108864: "6", 134217728: "5", 268435456: "4",
		536870912: "3", 1073741824: "2", 2147483648: "1", 4294967296: "0",
	}
	in := bufio.NewReader(os.Stdin)
	n := ReadNumber(in)
	blackList = make(Arrays, 0)
	whiteList = make(Arrays, 0)
	for i := 0; i < n; i++ {
		line, _ := in.ReadString('\n')
		addr_str := strings.TrimSpace(line[:len(line)-1])
		isBlackList := true
		if addr_str[0] == '+' {
			isBlackList = false
		}
		var cleanAddr []string
		x := 32
		if strings.ContainsAny(addr_str, "/") {
			splittedList := strings.Split(addr_str[1:], "/")
			cleanAddr = strings.Split(splittedList[0], ".")
			x, _ = strconv.Atoi(splittedList[1])
		} else {
			cleanAddr = strings.Split(addr_str[1:], ".")
		}
		addrNum := uint64(0)
		for i := 0; i < 4; i++ {
			atoi, _ := strconv.Atoi(cleanAddr[i])
			addrNum = addrNum + multipliers[i]*uint64(atoi)
		}
		addressRange := math.Pow(2, float64(32-x))
		if isBlackList {
			blackList = append(blackList, [2]uint64{addrNum, addrNum + uint64(addressRange) - 1})
		} else {
			whiteList = append(whiteList, [2]uint64{addrNum, addrNum + uint64(addressRange) - 1})
		}
	}
	sort.Sort(blackList)
	sort.Sort(whiteList)
	ipRanges = make([]string, 0)
	addIPs(0, (2<<31)-1)
	fmt.Println(len(ipRanges))
	fmt.Println(strings.Join(ipRanges, "\n"))
}

func addIPs(left, right uint64) {
	if checkList(blackList, left, right) {
		if checkList(whiteList, left, right) {
			if left == right {
				fmt.Println("-1")
				os.Exit(0)
			}
			boundary := left + ((right - left) / 2)
			addIPs(left, boundary)
			addIPs(boundary+1, right)
		} else {
			ipRanges = append(ipRanges, fmt.Sprintf("%s/%s", numberToAddress(left), ranges[right-left+1]))
		}
	}
}

func checkList(listToCheck Arrays, left, right uint64) bool {
	if len(listToCheck) > 0 {
		el := listToCheck[findIndex(listToCheck, left)]
		if (left <= el[0] && el[0] <= right) || (left <= el[1] && el[1] <= right) || (el[0] <= left && left <= el[1]) || (el[0] <= right && right <= el[1]) {
			return true
		}
	}
	return false
}

func findIndex(listToCheck Arrays, index uint64) int {
	left := 0
	right := len(listToCheck) - 1
	for {
		if left == right {
			return left
		}
		mid := left + ((right - left) / 2)
		if listToCheck[mid][0] <= index && index <= listToCheck[mid][1] {
			return mid
		}
		if listToCheck[mid][0] > index {
			right = mid
		} else {
			left = mid + 1
		}
	}
}

func numberToAddress(number uint64) string {
	addrParts := [4]string{}
	for i := 0; i < 4; i++ {
		left_mult := number / multipliers[i]
		addrParts[i] = strconv.Itoa(int(left_mult))
		number = number - (left_mult * multipliers[i])
	}
	return strings.Join(addrParts[:], ".")
}

func ReadNumber(in *bufio.Reader) int {
	line, _ := in.ReadString('\n')
	num, _ := strconv.Atoi(strings.TrimSpace(line[:len(line)-1]))
	return num
}
