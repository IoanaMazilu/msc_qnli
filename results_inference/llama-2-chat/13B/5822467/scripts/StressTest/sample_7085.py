annie_hours_premise = 10
annie_hours_hypothesis = 30

# the hypothesis refers to the number of hours Annie needs to do the job
if annie_hours_premise <= annie_hours_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'annie_hours_premise'
    label = "contradiction"
elif annie_hours_hypothesis!= annie_hours_premise:
    # check if the number of hours Annie needs to do the job in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
