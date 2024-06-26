earned_premise = 9000
earned_hypothesis = 9000

# the hypothesis refers to the amount he and Rick earned in one year, which is also mentioned in the premise
if earned_hypothesis < earned_premise:
    # check if the hypothesis value contradicts the amount of 'earned_premise'
    label = "contradiction"
elif earned_hypothesis > earned_premise:
    # check if the hypothesis value contradicts the amount of 'earned_premise'
    label = "contradiction"
else:
    # if the hypothesis value is the same as the premise, we can infer entailment
    label = "entailment"

print(label)
