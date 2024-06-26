age_premise = 85
age_hypothesis = 85

# the hypothesis mentions the age of Ariel Sharon, which is also mentioned in the premise
if age_hypothesis!= age_premise:
    # check if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
