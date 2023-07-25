# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2  (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)
my_list = ["pink", "red", "black", "pink", "black"]
# How To Whiteboard
# 1. Read the problem out loud 
# 2. Making any assumption, ask claryinging questions. (you are establishing good habits)
# 3. coming up with the approach (drawing pictures/ pseudo code) (make sure you dont leave us the viewers in the dust)
# 	- ideally, you can come up with a COUPLE solutions, evaluate their complexities/efficiency/then make your pick
# 4. Write out the code (this should actually take a small amount of time)
# 5. Debug / re-evaluate

#lowercase 
#step 1: define solutions and identified perams
#step 2: loop over the list and count the number of each color glove
#step 3: If ive seen the color we want to update the value in the dict. otherwise we create a new key value pair
#step 4: We will go over the dict. values and see how many pairs are possible.



def solution(color_gloves): 
    gloves = {}
    for color in color_gloves:
        if color in gloves: 
            gloves [color] += 1
        else:
            gloves [color] = 1
    pairs = 0
    for values in gloves.values():
          pairs += values // 2
    return pairs     
print(solution(my_list))












