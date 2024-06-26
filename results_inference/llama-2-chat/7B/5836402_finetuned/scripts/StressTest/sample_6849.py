apples_billy_premise = 10
apples_billy_hypothesis = 20

# the hypothesis refers to the number of apples Billy has, mentioned in the premise
if apples_billy_premise >= apples_billy_hypothesis:
    # check if the premise value contradicts the estimate of less than 'apples_billy_hypothesis'
    label = "contradiction"
elif apples_billy_premise < apples_billy_hypothesis:
    # if the premise value is less than the hypothesis estimate, we can infer entailment
    label = "entailment"
else:
    # if the premise value is equal to the hypothesis estimate, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
