number_premise = 7
number_hypothesis = 5

# the hypothesis refers to a number that is divisible by 2 and has 4 digits, as stated in the premise
if number_hypothesis >= number_premise:
    # check if the hypothesis value contradicts the estimate of 'number_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
