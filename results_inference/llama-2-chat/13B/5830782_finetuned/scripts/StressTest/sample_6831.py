girls_premise = 2
girls_hypothesis = 1

# the hypothesis refers to the number of girls mentioned in the premise
if girls_hypothesis >= girls_premise:
    # check if the hypothesis value contradicts the number of girls in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)