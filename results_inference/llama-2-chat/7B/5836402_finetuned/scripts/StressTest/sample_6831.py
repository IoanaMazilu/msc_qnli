girls_premise = 2
girls_hypothesis = 1

# the hypothesis refers to the number of girls, which is also mentioned in the premise
if girls_premise >= girls_hypothesis:
    # check if the estimate of 'girls_hypothesis' contradicts the number of girls in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
