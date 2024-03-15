class Items:

    def __init__(self,weight,value):
        self.value = value
        self.weight = weight

def fractionalKnapsack(w,arr):

    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)

    res = 0
    for item in arr:
        if item.weight <= w:
            w -= item.weight
            res += item.value
        else:
            res += item.value * w / item.weight
            break
    return res
    

if __name__ == "__main__":

	# Weight of Knapsack
	W = 50
	arr = [Items(60, 10), Items(100, 20), Items(120, 30)]

	# Function call
	max_val = fractionalKnapsack(W, arr)
	print ('Maximum value we can obtain = {}'.format(max_val))