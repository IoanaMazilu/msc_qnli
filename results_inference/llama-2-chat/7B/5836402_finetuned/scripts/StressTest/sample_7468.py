level_less_than_7_graduates_premise = 7
level_graduates_hypothesis = 1

# the hypothesis refers to the level of college graduates, which is also mentioned in the premise
if level_less_than_7_graduates_premise <= level_graduates_hypothesis:
    # check if the estimate of 'level_graduates_hypothesis' contradicts the level of graduates mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
