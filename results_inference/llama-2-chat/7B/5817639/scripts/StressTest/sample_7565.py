jill_work_premise = 8.00
jill_work_hypothesis = 8.00
tip_rate_premise = 0.3
tip_rate_hypothesis = 0.2

# the hypothesis talks about the tip rate, which is also mentioned in the premise
if jill_work_hypothesis <= jill_work_premise:
    # check if the hypothesis value contradicts the estimate of the tip rate in the premise
    label = "contradiction"
elif tip_rate_hypothesis < tip_rate_premise:
    # check if the estimated tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
