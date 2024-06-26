apples_premise = 360
apples_hypothesis = 460

# the hypothesis refers to the number of apples Anita has, which is also mentioned in the premise
if apples_hypothesis <= apples_premise:
    # check if the hypothesis value contradicts the premise
    label = "entailment"
elif apples_hypothesis > apples_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise, but not more than the premise, we can infer entailment
    label = "neutral"

print(label)
