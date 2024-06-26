euro_premise = "1999"
euro_hypothesis = "1999"

# the hypothesis talks about Sweden adopting the single European currency in 1999, which is also mentioned in the premise
if euro_hypothesis == euro_premise:
    # the hypothesis is entailed by the premise
    label = "entailment"
elif euro_hypothesis!= euro_premise:
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis contradicts the premise
    label = "contradiction"

print(label)
