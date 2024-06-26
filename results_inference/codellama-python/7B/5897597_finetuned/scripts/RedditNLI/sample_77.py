costs_increase_premise = 190
costs_increase_hypothesis = 190

# the hypothesis and premise mention the increase in labour costs due to minimum wage increases
if costs_increase_hypothesis!= costs_increase_premise:
    # check if the costs increase in the hypothesis contradicts the costs increase in the premise
    label = "contradiction"
else:
    # if the costs increase in the hypothesis does not contradict the costs increase in the premise, we can infer entailment
    label = "entailment"

print(label)
