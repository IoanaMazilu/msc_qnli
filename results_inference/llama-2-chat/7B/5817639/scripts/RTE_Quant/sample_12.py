participants_premise = 70e6
participants_hypothesis = 70e6

# the hypothesis talks about the number of participants in the pilgrimage, which is also mentioned in the premise
if participants_hypothesis == participants_premise:
    # if the hypothesis and premise values match, we can infer entailment
    label = "entailment"
elif participants_hypothesis > participants_premise:
    # if the number of participants in the hypothesis is greater than the number mentioned in the premise, we can infer entailment
    label = "entailment"
elif participants_hypothesis < participants_premise:
    # if the number of participants in the hypothesis is less than the number mentioned in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise values do not match, but do not contradict each other either, we can infer neutrality
    label = "neutral"

print(label)
