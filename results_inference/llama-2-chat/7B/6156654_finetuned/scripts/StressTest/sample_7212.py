scores_premise = [1, 2, 3, 4, 5]
scores_hypothesis = [8, 2, 3, 4, 5]

# the hypothesis refers to the scores in the premise
if scores_premise <= scores_hypothesis:
    # check if the scores in the premise contradict the scores in the hypothesis
    label = "contradiction"
elif scores_premise > scores_hypothesis:
    # check if the scores in the premise are greater than the scores in the hypothesis
    # this is entailed by the hypothesis
    label = "entailment"
else:
    # if the scores in the premise are equal to the scores in the hypothesis, we can infer entailment
    label = "neutral"

print(label)
