# Premise: Sara had 49.0 quarters in her bank and she spent 21.0 quarters.
# Hypothesis: She has 27.0 quarters now.
# Golden Label: contradiction

initial_quarters_premise = 49.0
spent_quarters_premise = 21.0
remaining_quarters_hypothesis = 27.0

# the hypothesis refers to the number of remaining quarters, which can be estimated from the premise
# compute the remaining quarters in the premise
remaining_quarters_premise = initial_quarters_premise - spent_quarters_premise
if remaining_quarters_hypothesis != remaining_quarters_premise:
    # check if the number of remaining quarters in the hypothesis contradicts the number of remaining quarters from the premise
    label = "contradiction"
else:
    # if the hypothesis values does not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

