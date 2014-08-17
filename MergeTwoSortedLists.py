def merge(l1,l2):
	""" assuming two lists are sorted in ascending order """
	l = []
	c1 = c2 = 0
	while c1 < len(l1) and c2 < len(l2):
		if l1[c1] < l2[c2]:
			l.append(l1[c1])
			c1 += 1
		else:
			l.append(l2[c2])
			c2 += 1
	l.extend(l1[c1:])
	l.extend(l2[c2:])
	l1 = [1,1,1,1,1,1,1]
	return l



if __name__ == "__main__":
	print merge([1,3,5], [2,4,6])
	print merge([2,3,8], [0,4,7])
	print merge([], [1,2,3])
