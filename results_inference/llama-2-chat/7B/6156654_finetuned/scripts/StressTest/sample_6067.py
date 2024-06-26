shops_premise = 5
shops_hypothesis = 4

# the hypothesis talks about the number of shops in the town, which is also mentioned in the premise
if shops_hypothesis >= shops_premise:
    # check if the number of shops in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the number of shops in the hypothesis is less than the premise, we can infer entailment
    label = "entailment"

print(label)
