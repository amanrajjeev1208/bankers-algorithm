#***************************************************************************
#****************************THE MAIN FUNCTION******************************
#***************************************************************************
def main():
	#Take the number of processes, number of different resources, maximum resources of each type(matrix) as input from user
	processes = int(input("number of processes : "))
	resources = int(input("number of resources : "))
	max_resources = [int(i) for i in input("maximum resources : ").split()]

	#Take the current allocation matrix input from the user
	print("\n-- allocated resources for each process --")
	currently_allocated = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

	#Take the maximum resources for each process matrix(tells how many resources the process needs for completion) input from the user
	print("\n-- maximum resources for each process --")
	max_need = [[int(i) for i in input(f"process {j + 1} : ").split()] for j in range(processes)]

	#Calculate the total allocated resources of each type
	allocated = [0] * resources
	for i in range(processes):
		for j in range(resources):
			allocated[j] += currently_allocated[i][j]
	print(f"\ntotal allocated resources : {allocated}")

	#Calculate the total available resources of each type
	available = [max_resources[i] - allocated[i] for i in range(resources)]
	print(f"total available resources : {available}\n")

	#Checking for Safe and Unsafe state of the process
	running = [True] * processes
	safeSeq = [0] * processes
	safeCount = 0
	count = processes
	while count != 0:
		safe = False
		for i in range(processes):
			if running[i]:
				executing = True
				for j in range(resources):
					if max_need[i][j] - currently_allocated[i][j] > available[j]:     #Unsafe state if the needs are not met
						executing = False
						break
				if executing:
					print(f"process {i + 1} is executing")
					running[i] = False     #mark the process as completed
					safeSeq[safeCount] = i + 1    #add the process into the safe sequence for output
					safeCount -= 1
					count -= 1
					safe = True            #mark the process safe
					#Add the resources allocated to that particular process to the availble resources matrix
					for j in range(resources):
						available[j] += currently_allocated[i][j]
					break
		if not safe:
			print("the processes are in an unsafe state.")
			break

		print(f"the process is in a safe state.\navailable resources : {available}\n")
	print(f"the safe sequence is : {safeSeq}\n")

#***************************************************************************
#****************************DRIVER CODE************************************
#***************************************************************************
if __name__ == '__main__':
	main()