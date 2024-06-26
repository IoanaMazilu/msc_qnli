kamal_work_premise = 20
kamal_work_hypothesis = 50

# the hypothesis talks about the number of days required to complete the work, referenced also in the premise
if kamal_work_hypothesis <= kamal_work_premise:
    # check if the hypothesis value contradicts the estimate of 'kamal_work_premise' days
    label = "contradiction"
elif kamal_work_premise == 20:
    # the premise gives only an estimate for the number of days required
    # any number of days greater than 'kamal_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
