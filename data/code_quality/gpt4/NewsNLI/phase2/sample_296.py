age_premise = 68
age_hypothesis = 68

# the hypothesis mentions the age of the person, which is also mentioned in the premise
if age_hypothesis != age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis does not contradict the age in the premise, we can infer entailment
    label = "entailment"

print(label)
