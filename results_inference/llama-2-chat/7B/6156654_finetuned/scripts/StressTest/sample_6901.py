offer_premise = 70
offer_hypothesis = 30
shirt_premise = 70
shirt_hypothesis = 70

# the hypothesis talks about the offer for shirts, which is also mentioned in the premise
if offer_hypothesis!= offer_premise:
    # check if the offer in the hypothesis contradicts the offer in the premise
    label = "contradiction"
elif shirt_hypothesis!= shirt_premise:
    # check if the number of shirts in the hypothesis contradicts the number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
