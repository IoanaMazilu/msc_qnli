jump_percentage_premise = 400
jump_percentage_hypothesis = 400

# the hypothesis and premise mention the jump percentage of Black Business Ownership in one year
if jump_percentage_hypothesis != jump_percentage_premise:
    # check if the jump percentage in the hypothesis contradicts the jump percentage in the premise
    label = "contradiction"
else:
    # if the jump percentage in the hypothesis does not contradict the jump percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
