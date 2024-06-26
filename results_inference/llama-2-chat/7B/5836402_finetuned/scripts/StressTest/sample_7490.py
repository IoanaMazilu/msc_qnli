apples_premise = 360
apples_hypothesis = 560

# the hypothesis refers to the number of apples Anita has, which is also mentioned in the premise
if apples_hypothesis!= apples_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
