work_ravi_premise = 24
work_ravi_hypothesis = 14
work_prakash_premise = 40
work_prakash_hypothesis = 40

# the hypothesis refers to the time taken by Ravi and Prakash to do a piece of work mentioned in the premise
if work_ravi_premise <= work_ravi_hypothesis:
    # check if the estimate of 'work_ravi_hypothesis' contradicts the time taken by Ravi in the premise
    label = "contradiction"
elif work_prakash_hypothesis != work_prakash_premise:
    # check if the time taken by Prakash in the hypothesis contradicts the time taken by Prakash reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
