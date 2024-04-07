# Premise: If the ratio of their ages is 7:9, how old is Sandy?
# Hypothesis: If the ratio of their ages is more than 6:9, how old is Sandy?
# Golden Label: entailment

ratio_premise = 7/9
ratio_hypothesis = 6/9

# the hypothesis refers to the age ratio mentioned in the premise
if ratio_premise <= ratio_hypothesis:
    # check if the 'ratio_hypothesis' contradicts the ratio presented in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

