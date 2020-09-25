import time

def merge(list_numbers,start1, end1, start2, end2,draw_in_canvas, time_chosen):
	
	data = []
	start_1,start_2 = start1,start2

	while start1<=end1 and start2<=end2:
		if list_numbers[start1]<list_numbers[start2]:
			data.append(list_numbers[start1])
			start1 += 1
		else:
			data.append(list_numbers[start2])
			start2 += 1
	while start1<=end1:
		data.append(list_numbers[start1])
		start1 += 1
	while start2<=end2:
		data.append(list_numbers[start2])
		start2 += 1

	start1, k = start_1, 0
	for i in range(start1,end2+1):
		list_numbers[i] = data[k]
		k += 1	

	colorArray = generate(len(list_numbers),start_1, end1, start_2, end2)
	draw_in_canvas(list_numbers,colorArray)
	time.sleep(time_chosen)
			
def generate(lenlist,start1, end1, start2, end2):
	colorArray = []
	for i in range(lenlist):
		colorArray.append('red')
		if i>=start1 and i<=end1:
			colorArray[i] = 'brown'
		elif i>=start2 and i<= end2:
			colorArray[i] = 'purple'
	return colorArray

def merge_sort(list_numbers, head, tail, draw_in_canvas,time_chosen):
	if head<tail:
		mid = (head+tail)//2
		merge_sort(list_numbers,head,mid, draw_in_canvas, time_chosen)

		merge_sort(list_numbers,mid+1, tail, draw_in_canvas, time_chosen)

		merge(list_numbers, head, mid, mid+1, tail, draw_in_canvas, time_chosen)
		
	draw_in_canvas(list_numbers,['green']*len(list_numbers))

