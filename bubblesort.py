import time

def bubble_sort(list_numbers, draw_in_canvas, time_chosen,colorArray):

	for i in range(len(list_numbers)):
		for j in range(i+1, len(list_numbers)):
			if list_numbers[i] > list_numbers[j]:
				list_numbers[i],list_numbers[j] = list_numbers[j], list_numbers[i]
				colorArray[i], colorArray[j]  = 'green','green'
				draw_in_canvas(list_numbers,colorArray)
				time.sleep(time_chosen)
				colorArray[i], colorArray[j]  = 'red','red'
		colorArray[i] = 'green';
	draw_in_canvas(list_numbers,['green']*len(list_numbers))
