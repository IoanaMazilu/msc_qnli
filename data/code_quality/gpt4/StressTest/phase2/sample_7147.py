num_premise = 8
num_hypothesis = 4

# the hypothesis refers to the number Cindy is thinking of which is also mentioned in the premise
if num_hypothesis >= num_premise:
    # check if the number in the hypothesis contradicts the estimate of less than 'num_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number
    # any number less than 'num_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
