# Premise: Jefferson County Deputy Sheriff Rod Carroll said that at least 80 and as many as 120 injured people were taken from the scene.
# Hypothesis: As many as 120 injured were taken to hospitals.
# Golden Label: entailment

min_injured_premise = 80
max_injured_premise = 120
max_injured_hypothesis = 120

# the hypothesis refers to the maximum number of people injured which is also mentioned in the premise
if max_injured_hypothesis > max_injured_premise:
    # check if the maximum number of injured people from the hypothesis contradicts the maximum number of injured people in the premise
    label = "contradiction"
else:
    # if the maximum number of injured people from the hypothesis does not contradict the maximum number of injured people in the premise, we can infer entailment
    label = "entailment"

print(label)

