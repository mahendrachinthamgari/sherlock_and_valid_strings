from collections import Counter
def sherlock_string(s):
	d = list(Counter(Counter(s).values()).values()))
	if len(d) == 1:
		return "Yes"
	elif len(d) == 2:
		c = d.pop()
		if c > 1:
			return "No"
		else:
			return "Yes"
	else:
		return "NO"
	
	
	
