billy_apples_premise = 10
billy_apples_hypothesis = 20

# the hypothesis talks about the number of apples Billy has, referenced also in the premise
if billy_apples_premise >= billy_apples_hypothesis:
    # check if the number of apples in the premise contradicts the estimate of less than 'billy_apples_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
