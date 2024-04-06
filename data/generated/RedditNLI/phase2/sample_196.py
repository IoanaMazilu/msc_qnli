# Premise: Unemployment falls in seven swing states.
# Hypothesis: Unemployment falls in 41 states in September.
# Golden Label: neutral

states_unemployment_fall_premise = 7
states_unemployment_fall_hypothesis = 41

# the hypothesis and premise mention the number of states in which unemployment falls
if states_unemployment_fall_hypothesis < states_unemployment_fall_premise:
    # check if the number of states in the hypothesis contradicts the number of states in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

