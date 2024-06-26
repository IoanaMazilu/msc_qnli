sacha_speed_premise = 9
sacha_speed_hypothesis = 1
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis refers to the running speeds of Sacha and Bruno, as mentioned in the premise
if sacha_speed_premise <= sacha_speed_hypothesis:
    # check if the estimate of 'sacha_speed_hypothesis' contradicts the Sacha's speed in the premise
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # check if the Bruno's speed in the hypothesis contradicts the Bruno's speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
