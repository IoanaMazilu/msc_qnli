ratio_age_premise = 7/9
ratio_age_hypothesis = 5/9

# the hypothesis refers to the ratio of their ages as mentioned in the premise
if ratio_age_premise <= ratio_age_hypothesis:
    # check if the 'ratio_age_hypothesis' contradicts the ratio of their ages in the premise
    label = "contradiction"
else:
    # if the 'ratio_age_hypothesis' does not contradict the 'ratio_age_premise', we can infer entailment
    label = "entailment"

print(label)
