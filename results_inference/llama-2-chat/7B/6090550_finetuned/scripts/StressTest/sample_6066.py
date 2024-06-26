shops_premise = 4 to 5
shops_hypothesis = 5 to 5

# the hypothesis talks about the number of shops in the town, which is also mentioned in the premise
if shops_hypothesis <= shops_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
