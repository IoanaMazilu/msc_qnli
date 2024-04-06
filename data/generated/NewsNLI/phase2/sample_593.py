# Premise: The two who were injured by gunshots were transported to out-of-area hospitals and are in critical condition, Barnes told reporters.
# Hypothesis: Two people are injured, in critical condition, the police chief says.
# Golden Label: neutral

injured_premise = 2
injured_hypothesis = 2

# the hypothesis mentions the number of people injured and in critical condition, which is also referenced in the premise
if injured_hypothesis != injured_premise:
    # check if the number of people injured in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the number of injured people from the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

