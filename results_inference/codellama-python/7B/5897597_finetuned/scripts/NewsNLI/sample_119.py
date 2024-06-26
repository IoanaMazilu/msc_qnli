age_premise = 6
age_hypothesis = 6

# the hypothesis mentions the age of Dylan, which is also mentioned in the premise
if age_hypothesis!= age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis does not contradict the age in the premise, we can infer entailment
    label = "entailment"

print(label)
