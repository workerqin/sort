#!/usr/bin/python
#-*_ coding:utf-8-*-



#插入排序
def insert_sort(lists):
	size = len(lists)	
	for i in range(1, size):
		j = i-1
		sort_key = lists[i]
		while j >= 0:
			if lists[j] > sort_key:
				lists[j+1] = lists[j]
				lists[j] = sort_key
			j-=1
	return lists

#希尔排序
def shell_sort(lists):
	size = len(lists)
	step = 2
	group = size/step
	while group > 0:
		for i in range(0, group):
			j = i + group
			while j < size:
				k = j - group
				key = lists[j]
				while k >= 0:
					if lists[k] > key:
						lists[k + group] = lists[k]
						lists[k] = key
					k -= group
				j += group
		group/=step
	return lists


#冒泡排序
def bubble_sort(lists):
	size = len(lists)
	for i in range(0, size):
		for j in range(i+1, size):	
			if lists[i] > lists[j]:
				lists[i], lists[j] = lists[j], lists[i]
	return lists


#快速排序
def quick_sort(lists, left, right):
	if left >= right:
		return lists	
	key = lists[left]
	low = left
	high = right
	while left < right:
		while left < right and lists[right] >= key:
			right -= 1
		lists[left] = lists[right]
		while left < right and lists[left] <= key:
			left += 1
		lists[right] = lists[left]
	lists[left] = key
	quick_sort(lists, low, right - 1)
	quick_sort(lists, right+1, high)
	return lists

#直接选择排序
def select_sort(lists):
	size = len(lists)
	for i in range(0, size):
		min = lists[i]
		for j in range(i+1, size):
			if lists[j] < min:
				min = lists[j]	
				lists[i], lists[j] = lists[j], lists[i]
	return lists

if __name__ == "__main__":
	select_array = [51,33,62,96,87,17,28,51]
	#sort_array = quick_sort(select_array, 0, len(select_array)-1)
	sort_array = select_sort(select_array)
	print sort_array
	
