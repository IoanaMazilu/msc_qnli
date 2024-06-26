weeks_premise = 3
weeks_hypothesis = 6

# the hypothesis refers to the number of weeks Rikki has been going to the gym, which is also mentioned in the premise
if weeks_premise <= weeks_hypothesis:
    # check if the estimate of 'weeks_hypothesis' contradicts the number of weeks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
