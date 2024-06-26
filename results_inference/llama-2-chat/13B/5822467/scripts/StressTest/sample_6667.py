kamal_work_premise = 40
kamal_work_hypothesis = 20

# the hypothesis refers to the number of days required to complete the work, mentioned in the premise
if kamal_work_premise > kamal_work_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'less than 40 days' in the premise
    label = "contradiction"
elif kamal_work_hypothesis == 0:
    # check if the hypothesis value is inconsistent with the premise
    label = "contradiction"
else:
    # if the hypothesis value is consistent with the premise, we can infer entailment
    label = "entailment"

print(label)
