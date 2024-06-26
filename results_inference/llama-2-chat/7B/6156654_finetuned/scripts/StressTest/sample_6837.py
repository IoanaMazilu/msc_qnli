earned_premise = 9000
earned_hypothesis = 4000

# the hypothesis refers to the amount of money earned by he and Rick, which is also mentioned in the premise
if earned_hypothesis >= earned_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif earned_hypothesis < earned_premise:
    # check if the hypothesis value is less than the premise value
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
