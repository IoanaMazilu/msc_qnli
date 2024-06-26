states_civil_unions_premise = 5
states_civil_unions_hypothesis = 5

# the hypothesis mentions the number of states that allow civil unions for same-sex couples, which is also referenced in the premise
if states_civil_unions_hypothesis != states_civil_unions_premise:
    # check if the number of states allowing civil unions in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the number of states from the hypothesis does not contradict the number of states in the premise, we can infer entailment as there's no additional info in hypothesis
    label = "entailment"

print(label)
