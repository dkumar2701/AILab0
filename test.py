import student_code

tests_passed = 0

start_array = [-4, 5, -3, -19]
final_array = [-19, -4, -3, 5]
start_stats = [0, 0, 0] #-5.25 mean
final_stats = [-6, -4, -19]

print("\n\rrunning test 6")
print("input data",start_array)
student_code.order(start_array,start_stats)
print("student sorted data",start_array)
print("expected data", final_array)
print("student stats",start_stats)
print("expected stats", final_stats)
grade=2

if len(start_array)==len(final_array):
	tests_passed=tests_passed+1
	print("size test passed")
	grade=1
	for x in range(len(start_array)):
		if start_array[x]!=final_array[x]:
			grade=0
	if grade==1:
		print("sorted array passed")
		tests_passed=tests_passed+1
	else:
		print("sorted array failed")
	grade=1
	for x in range(len(start_stats)):
		if start_stats[x]!=final_stats[x]:
			grade=0
	if grade==1:
		print("stats passed")
		tests_passed=tests_passed+1
	else:
		print("stats failed")
else:
	print("size test failed")
	
start_array = [1, 0]
final_array = [0, 1]
start_stats = [0, 0, 0]
final_stats = [0, 0, 0]

print("\n\rrunning test 6")
print("input data",start_array)
student_code.order(start_array,start_stats)
print("student sorted data",start_array)
print("expected data", final_array)
print("student stats",start_stats)
print("expected stats", final_stats)
grade=2

if len(start_array)==len(final_array):
	tests_passed=tests_passed+1
	print("size test passed")
	grade=1
	for x in range(len(start_array)):
		if start_array[x]!=final_array[x]:
			grade=0
	if grade==1:
		print("sorted array passed")
		tests_passed=tests_passed+1
	else:
		print("sorted array failed")
	grade=1
	for x in range(len(start_stats)):
		if start_stats[x]!=final_stats[x]:
			grade=0
	if grade==1:
		print("stats passed")
		tests_passed=tests_passed+1
	else:
		print("stats failed")
else:
	print("size test failed")
	
start_array = [0, 1, 2]
final_array = [0, 1, 2]
start_stats = [0, 0, 0]
final_stats = [1, 1, 0]

print("\n\rrunning test 6")
print("input data",start_array)
student_code.order(start_array,start_stats)
print("student sorted data",start_array)
print("expected data", final_array)
print("student stats",start_stats)
print("expected stats", final_stats)
grade=2

if len(start_array)==len(final_array):
	tests_passed=tests_passed+1
	print("size test passed")
	grade=1
	for x in range(len(start_array)):
		if start_array[x]!=final_array[x]:
			grade=0
	if grade==1:
		print("sorted array passed")
		tests_passed=tests_passed+1
	else:
		print("sorted array failed")
	grade=1
	for x in range(len(start_stats)):
		if start_stats[x]!=final_stats[x]:
			grade=0
	if grade==1:
		print("stats passed")
		tests_passed=tests_passed+1
	else:
		print("stats failed")
else:
	print("size test failed")



print("Tests passed: ", tests_passed, "\n")
