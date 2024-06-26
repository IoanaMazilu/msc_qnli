suresh_efficiency_premise = 25
suresh_efficiency_hypothesis = 35

# the hypothesis refers to the efficiency of Suresh mentioned in the premise
if suresh_efficiency_premise >= suresh_efficiency_hypothesis:
    # check if the estimate of'suresh_efficiency_hypothesis' contradicts the efficiency of Suresh in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
