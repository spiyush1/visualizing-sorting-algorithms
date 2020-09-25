from tkinter import *
from tkinter import ttk
import random as rd
from bubblesort import bubble_sort
from quicksort import quick_sort
from mergesort import merge_sort

root = Tk()
root.title("Sorting Algorithm Visualizer")
frame = LabelFrame(root, height = 400, width = 300, padx = 10, pady = 10, bg = 'grey')
frame.grid(row = 0, column = 1, sticky = N+S)

canvas = Canvas(root, height = 400, width = 400, relief = SUNKEN, bg = 'white')
canvas.grid(row = 0, column = 0, padx = 10)

# variables
selected_algo = StringVar()
list_numbers = []
colorArray=[]

# canvas
def draw_in_canvas(list_numbers,colorArray):
	canvas.delete('all')
	c_height, c_width = 350, 350.0
	x_width = c_width/(len(list_numbers)+1)
	offset = 30.0
	spacing = 10.0
	m = max(list_numbers)
	for i,j in enumerate(list_numbers):
		x0 = i*x_width + offset + spacing
		y0 = 400- j/m *c_height
		x1 = (i+1)*x_width + offset
		y1 = 400

		canvas.create_rectangle(x0,y0,x1,y1, fill = colorArray[i])
		canvas.create_text(x0, y0, anchor = SW, text = str(j))
	colorArray = ['red']*len(list_numbers)
	root.update_idletasks()

# Generating random array
def gener(max_number, min_number, size_array):
	global list_numbers
	global colorArray

	list_numbers.clear()
	colorArray.clear()
	for i in range(size_array):
		x = rd.randint(min_number,max_number)
		list_numbers.append(x)
	colorArray = ['red']*len(list_numbers)
	draw_in_canvas(list_numbers,colorArray)

# starting desired algorithm
def startAlgo():
	global list_numbers
	global selected_algo
	global speedscale
	global colorArray

	if selected_algo.get()==av_list[0]:
		bubble_sort(list_numbers,draw_in_canvas,float(speedscale.get()),colorArray)
	elif selected_algo.get()==av_list[1]:
		merge_sort(list_numbers,0, len(list_numbers)-1,draw_in_canvas,float(speedscale.get()))
	else:
		quick_sort(list_numbers,0,len(list_numbers)-1,draw_in_canvas,float(speedscale.get()))

# available algorithms for comparison
av_list = ['Bubble Sort', 'Merge Sort', 'Quick Sort']
selected_algo.set(av_list[0])

my_label = Label(frame,text = "Algorithm: ", bg = 'grey')
my_label.grid(row = 0, column = 0, sticky = W)

for i in av_list:
	Radiobutton(frame, text = i, variable = selected_algo, value = i, bg = 'grey').grid(row = av_list.index(i)+1, column = 0, sticky = W)

speedscale = Scale(frame, from_= 0.0 , to = 2.0, length = 200, digits = 2, resolution = 0.1, orient = HORIZONTAL, label ="Select speed(s):")
speedscale.grid(row = 4, column = 0)

# input1 = Entry(frame)
input1 = Scale(frame, orient = HORIZONTAL , from_= 5 , to = 50, length = 200, resolution = 1.0, label = "Size:")
input1.grid(row = 6, column = 0, pady = 10)

input2 = Scale(frame, orient = HORIZONTAL , from_= 5 , to = 1000, length = 200, resolution = 1.0, label = "Min Value:")
input2.grid(row = 8, column = 0, pady = 10)

input3 = Scale(frame, orient = HORIZONTAL , from_= 5 , to = 1000, length = 200, resolution = 1.0, label = "Max Value:")
input3.grid(row = 10, column = 0, pady = 10)

button = Button(frame, text = "Generate Array", command = lambda:gener(int(input3.get()),int(input2.get()), int(input1.get())))
button.grid(row = 11, column = 0, sticky = W)

button2 = Button(frame, text = "Sort", command = startAlgo, width = 4, height = 2)
button2.grid(row = 0, column = 0, sticky = E)
root.mainloop()
