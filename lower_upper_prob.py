def sanitize_result(list):
		rslt = []
		for i in list:
				x,y = i.split("->")
				if x == y:
					rslt.append(x)
				else:  
					rslt.append(i)
		return rslt

def solve(input_list, lower, upper):
		# assuming list is already sorted
		help_list = []
		for i in input_list:
				if i >= lower and i<=upper:
						help_list.append(i)

		if len(help_list)==0 :
				rslt_list =  [str(lower) + "->" + str(upper)]
				return sanitize_result(rslt_list)

		result = []
		if help_list[0] > lower:
				result.append(str(lower) + "->" + str(help_list[0]-1))

		for i in range(1,len(input_list)):
				if input_list[i] - input_list[i-1] > 1: # if diff is more than 1
						result.append(str(input_list[i-1]+1) + "->" + str(input_list[i]-1)) 

		if help_list[len(help_list)-1] != upper:
				result.append(str(help_list[len(help_list)-1]+1) + "->" + str(upper))

		return sanitize_result(result) 

if __name__=="__main__":
		lower, upper = 0, 99
		input_list =  [0, 1, 3, 50, 75]   
		print(solve(input_list, lower, upper))
