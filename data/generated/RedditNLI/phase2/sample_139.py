# Premise: FDIC Seizes 6 George Banks, Estimated Cost to FDIC: $807m.
# Hypothesis: FDIC seizes 6 Georgia banks, estimated losses of $807m.
# Golden Label: entailment

banks_premise = 6
banks_hypothesis = 6
estimated_cost_premise = 807
estimated_cost_hypothesis = 807

# the hypothesis and premise mention the number of banks FDIC seized and the estimated cost
if banks_premise != banks_hypothesis:
    # check if the number of banks in the hypothesis contradicts the number of banks in the premise
    label = "contradiction"
elif estimated_cost_premise != estimated_cost_hypothesis:
    # check if the estimated cost in the hypothesis contradicts the estimated cost in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

