prize_value_premise = 1000000
prize_value_hypothesis = 1000000

# the hypothesis mentions the value of the Automotive X Prize, which is also mentioned in the premise
if prize_value_hypothesis!= prize_value_premise:
    # check if the prize value in the hypothesis contradicts the prize value reported in the premise
    label = "contradiction"
else:
    # if the prize value in the hypothesis does not contradict the prize value in the premise, we can infer entailment
    label = "entailment"

print(label)
