men_employed_premise = 100
men_employed_hypothesis = 600

# the hypothesis refers to the number of men employed by NHAI mentioned in the premise
if men_employed_premise >= men_employed_hypothesis:
    # check if the estimate of'men_employed_hypothesis' contradicts the number of men employed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
