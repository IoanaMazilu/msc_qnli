# Premise: Three of the patients were in critical condition, two in serious, the department said.
# Hypothesis: Three people are in critical condition.
# Golden Label: neutral

critical_condition_premise = 3
critical_condition_hypothesis = 3

# the hypothesis mentions the number of people in critical condition, which is also mentioned in the premise
if critical_condition_hypothesis != critical_condition_premise:
    # check if the number of people in critical condition in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the number of people in critical condition in the hypothesis does not contradict the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)

