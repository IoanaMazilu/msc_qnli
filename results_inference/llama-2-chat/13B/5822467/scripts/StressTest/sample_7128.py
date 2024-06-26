anup_premise = 7/12
anup_hypothesis = 4/12
t_premise = T

# the hypothesis refers to the fraction of the sum of money that Anup was asked to find
if anup_hypothesis <= anup_premise:
    # check if the estimate of 'anup_hypothesis' contradicts the fraction of the sum of money mentioned in the premise
    label = "contradiction"
elif t_premise!= anup_premise:
    # check if the amount of money mentioned in the hypothesis contradicts the amount of money mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
