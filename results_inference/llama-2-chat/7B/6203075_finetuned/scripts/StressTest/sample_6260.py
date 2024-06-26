hours_premise = 15
hours_hypothesis = 15

# the hypothesis refers to the time Dan can take to do a job alone, which is also mentioned in the premise
if hours_hypothesis >= hours_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, we can infer entailment
    label = "entailment"

print(label)
