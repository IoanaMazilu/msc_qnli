quarters_initial_premise = 760
quarters_received_premise = 418
quarters_hypothesis = 1178.0

# the hypothesis refers to the number of quarters, which are also mentioned in the premise
# compute the total number of quarters in the premise
total_quarters_premise = quarters_initial_premise + quarters_received_premise
if quarters_hypothesis != total_quarters_premise:
    # check if the number of quarters in the hypothesis contradicts the number of quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
