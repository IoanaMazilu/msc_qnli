total_pears_premise = 101.0

if total_pears_premise!= total_pears_hypothesis:
    # check if the total number of pears from the hypothesis contradicts the total number of pears from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
