import time

def partition(list_numbers, head, tail, draw_in_canvas, time_chosen):
	ptr = head
	pivot = list_numbers[tail]

	for i in range(head, tail):
		if list_numbers[i]<=pivot:
			draw_in_canvas(list_numbers,color(len(list_numbers),ptr, i,tail, True))
			time.sleep(time_chosen)
			list_numbers[i], list_numbers[ptr] = list_numbers[ptr], list_numbers[i]
			ptr = ptr + 1

	draw_in_canvas(list_numbers,color(len(list_numbers),ptr, tail,tail, True))
	time.sleep(time_chosen)
	list_numbers[ptr], list_numbers[tail] = list_numbers[tail],list_numbers[ptr]
	return ptr

def quick_sort(list_numbers, head, tail, draw_in_canvas, time_chosen):
	if head < tail:
		partitionidx = partition(list_numbers, head, tail, draw_in_canvas, time_chosen)

		#left partition
		quick_sort(list_numbers, head, partitionidx-1, draw_in_canvas, time_chosen)

		# right partition
		quick_sort(list_numbers, partitionidx+1, tail, draw_in_canvas, time_chosen)

		draw_in_canvas(list_numbers, ['green']*len(list_numbers))

def color(lenlist, first,second,pivot, is_swapping= False):
	colorArray = []
	for i in range(lenlist):
		colorArray.append('grey')
		if i==first or i == second:
			colorArray[i] = 'red'
		if i==pivot:
			colorArray[i] = 'purple'
	return colorArray
