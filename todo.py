import sys

command_arg = sys.argv[1]
arg_list = sys.argv[2:]

file = "todo.txt"

def add(task_list):
	todo_file = open(file, 'a')
	for task in task_list:
		todo_file.write(task + '\n')
	todo_file.close()

def rm(index_list):
	index_list = [int(x) for x in index_list]
	todo_file = open(file, 'r')
	lines = todo_file.readlines()
	todo_file.close()

	for i in index_list:
		del lines[i-1]

	new_file = open(file, 'w+')
	for line in lines:
		new_file.write(line)
	new_file.close()

def strike(text):
	result = ''
	for c in text:
		result = result + c + '\u0336'
	return result

def done(index_list):
	index_list = [int(x) for x in index_list]
	todo_file = open(file, 'r')
	lines = todo_file.readlines()
	for i in index_list:
		lines[i-1] = strike(lines[i-1])

	new_file = open(file, 'w+')
	for line in lines:
		new_file.write(line)
	new_file.close()

def printer():
	todo_file = open(file, 'r')
	tasks = todo_file.readlines()
	for i, task in enumerate(tasks):
		print(i+1, task)

if command_arg == "add":
	add(arg_list)

if command_arg == "rm":
	rm(arg_list)

if command_arg == "done":
	done(arg_list)

printer()