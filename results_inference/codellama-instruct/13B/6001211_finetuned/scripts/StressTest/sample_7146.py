number_difference_premise = 4
number_difference_hypothesis = 8

# the hypothesis refers to the difference between the number Cindy is thinking of and the square of a positive integer
if number_difference_hypothesis < number_difference_premise:
    # check if the difference in the hypothesis contradicts the difference in the premise
    label = "contradiction"
elif number_difference_hypothesis > number_difference_premise:
    # check if the difference in the hypothesis is greater than the difference in the premise
    label = "entailment"
else:
    # if the difference in the hypothesis is equal to the difference in the premise, we can infer neutrality
    label = "neutral"

print(label)
