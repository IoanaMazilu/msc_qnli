estimated_return_premise = 5 to 10%
returned_art_hypothesis = 5 to 10%

# the hypothesis talks about the same percentage range as the premise
if returned_art_hypothesis == estimated_return_premise:
    # if the hypothesis and premise values match, we can infer entailment
    label = "entailment"
elif returned_art_hypothesis < estimated_return_premise:
    # if the hypothesis value is smaller than the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise values are equal or do not contradict each other, we can infer neutrality
    label = "neutral"

print(label)
