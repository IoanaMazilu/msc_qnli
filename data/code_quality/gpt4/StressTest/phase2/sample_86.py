china_workers_premise = 100
china_workers_hypothesis = 100

# the hypothesis talks about the number of workers from China in Richard's office, referenced also in the premise
if china_workers_premise > china_workers_hypothesis:
    # check if the number of China workers in the premise contradicts the estimate of more than 'china_workers_hypothesis'
    label = "contradiction"
elif china_workers_premise == china_workers_hypothesis:
    # the premise gives a precise number of China workers
    # any estimate of more than 'china_workers_hypothesis' is not consistent with the premise and cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
