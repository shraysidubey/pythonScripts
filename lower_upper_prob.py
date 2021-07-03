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

		for i in range(1,len(help_list)):
				if help_list[i] - help_list[i-1] > 1: # if diff is more than 1
						result.append(str(help_list[i-1]+1) + "->" + str(help_list[i]-1)) 

		if help_list[len(help_list)-1] != upper:
				result.append(str(help_list[len(help_list)-1]+1) + "->" + str(upper))

		return sanitize_result(result) 

if __name__=="__main__":
		lower, upper = 39, 83
		input_list =  [1,2,3,15,17,81,99,103]   
		print(solve(input_list, lower, upper))
