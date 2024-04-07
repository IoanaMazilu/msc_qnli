# Premise: While Kiran playing all but 3 got destroyed.
# Hypothesis: While Kiran playing all but 8 got destroyed.
# Golden Label: contradiction

destroyed_premise = 3
destroyed_hypothesis = 8

# the hypothesis talks about the number of items destroyed while Kiran was playing, referenced also in the premise
if destroyed_hypothesis != destroyed_premise:
    # check if the number of items destroyed in the hypothesis contradicts the number of items destroyed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

