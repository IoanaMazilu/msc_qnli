# Premise: Five other people were injured, and two of them were in critical condition, hospital officials said.
# Hypothesis: Two of the wounded are in critical condition.
# Golden Label: entailment

injured_people_premise = 5
critical_condition_premise = 2
critical_condition_hypothesis = 2

# the hypothesis refers to the number of people in critical condition, which is also mentioned in the premise
if critical_condition_hypothesis != critical_condition_premise:
    # check if the number of people in critical condition in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis and premise numbers do not contradict, we can infer entailment
    label = "entailment"

print(label)

