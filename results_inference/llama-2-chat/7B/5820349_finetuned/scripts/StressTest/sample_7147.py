number_premise = 8
number_hypothesis = 4

# the hypothesis refers to the number Cindy is thinking of, which is also mentioned in the premise
if number_hypothesis >= number_premise:
    # check if the hypothesis value contradicts the estimate of 'number_premise' less than
    label = "contradiction"
elif number_hypothesis < number_premise:
    # if the hypothesis value is less than 'number_premise', it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
