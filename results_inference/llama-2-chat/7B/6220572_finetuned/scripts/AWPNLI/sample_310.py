quarters_premise = 21.0
quarters_hypothesis = 70.0

# the hypothesis refers to the total number of quarters, which is also mentioned in the premise
if quarters_hypothesis!= quarters_premise + quarters_hypothesis:
    # check if the total number of quarters in the hypothesis contradicts the total number of quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
