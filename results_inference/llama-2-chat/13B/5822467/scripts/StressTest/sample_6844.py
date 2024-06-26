sacha_speed_premise = 4
sacha_speed_hypothesis = 7
bruno_speed_premise = 4
bruno_speed_hypothesis = 5

# the hypothesis refers to the speed of Sacha and Bruno mentioned in the premise
if sacha_speed_premise <= sacha_speed_hypothesis and bruno_speed_premise <= bruno_speed_hypothesis:
    # check if the estimate of'sacha_speed_hypothesis' and 'bruno_speed_hypothesis' contradict the speeds reported in the premise
    label = "contradiction"
elif sacha_speed_hypothesis!= bruno_speed_hypothesis:
    # check if the speed of Sacha and Bruno in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
