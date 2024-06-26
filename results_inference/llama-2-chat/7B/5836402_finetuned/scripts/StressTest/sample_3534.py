t_shirts_bought_premise = 8
t_shirts_bought_hypothesis = 3

# the hypothesis refers to the number of t-shirts bought by Sanoop mentioned in the premise
if t_shirts_bought_premise <= t_shirts_bought_hypothesis:
    # check if the estimate of 't_shirts_bought_hypothesis' contradicts the number of t-shirts bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
