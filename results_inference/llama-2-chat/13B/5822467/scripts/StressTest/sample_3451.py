joses_join_premise = 8
joses_join_hypothesis = 2

# the hypothesis refers to the time Jose joined and the amount of investment
if joses_join_premise <= joses_join_hypothesis:
    # check if the hypothesis value contradicts the estimate of less than 'joses_join_premise'
    label = "contradiction"
elif joses_join_hypothesis!= joses_join_premise:
    # check if the hypothesis value contradicts the amount of investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
