age_premise = 19
age_hypothesis = 19

# the hypothesis mentions the same age as the premise
if age_hypothesis!= age_premise:
    # check if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis does not contradict the age in the premise, we can infer entailment
    label = "entailment"

print(label)
