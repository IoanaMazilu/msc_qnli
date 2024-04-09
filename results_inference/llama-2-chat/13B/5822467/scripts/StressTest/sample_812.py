sacha_speed_premise = 6
bruno_speed_premise = 5
sacha_speed_hypothesis = 3
bruno_speed_hypothesis = 5

# the hypothesis refers to the speeds of Sacha and Bruno mentioned in the premise
if sacha_speed_premise <= sacha_speed_hypothesis and bruno_speed_premise <= bruno_speed_hypothesis:
    # check if the estimate of'sacha_speed_hypothesis' and 'bruno_speed_hypothesis' contradict the speeds reported in the premise
    label = "contradiction"
elif sacha_speed_hypothesis!= sacha_speed_premise or bruno_speed_hypothesis!= bruno_speed_premise:
    # check if the speeds in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
