# Premise: 3000 and Christine's share is Rs.
# Hypothesis: more than 1000 and Christine's share is Rs.
# Golden Label: entailment

share_premise = 3000
share_hypothesis = 1000

# the hypothesis refers to Christine's share mentioned in the premise
if share_premise <= share_hypothesis:
    # check if the estimate of 'share_hypothesis' contradicts Christine's share in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

