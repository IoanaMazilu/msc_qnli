girls_premise = 2
girls_hypothesis = 2

# the hypothesis refers to the number of girls going on a date with boys mentioned in the premise
if girls_hypothesis >= girls_premise:
    # check if the estimate of 'girls_hypothesis' contradicts the number of girls in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
