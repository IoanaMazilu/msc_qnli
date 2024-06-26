number_difference_premise = 4
number_difference_hypothesis = 8

# the hypothesis refers to the difference between the number Cindy is thinking of and the square of a positive integer mentioned in the premise
if number_difference_premise > number_difference_hypothesis:
    # check if the 'number_difference_premise' contradicts the 'number_difference_hypothesis'
    label = "contradiction"
elif number_difference_premise < number_difference_hypothesis:
    # check if the 'number_difference_premise' is less than the 'number_difference_hypothesis'
    label = "entailment"
else:
    # if the 'number_difference_premise' is equal to the 'number_difference_hypothesis', it is neutral
    label = "neutral"

print(label)
