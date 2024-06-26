jack_speed_premise = 7
jack_speed_hypothesis = 8
christina_speed_premise = 8
christina_speed_hypothesis = 8

# the hypothesis refers to the speeds of Jack and Christina which are also mentioned in the premise
if jack_speed_hypothesis <= jack_speed_premise:
    # check if the estimate of 'jack_speed_hypothesis' contradicts Jack's speed in the premise
    label = "contradiction"
elif christina_speed_hypothesis != christina_speed_premise:
    # check if Christina's speed in the hypothesis contradicts her speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
