total_quarters_premise = 21.0 + 49.0
total_quarters_hypothesis = 70.0

if total_quarters_hypothesis!= total_quarters_premise:
    # check if the number of quarters in the hypothesis contradicts the number of quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
