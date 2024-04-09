job_pay_premise = 75000
job_pay_hypothesis = 45000
commission_hypothesis = 45000 * 0.15

# the hypothesis refers to the estimated commission in the premise
if job_pay_hypothesis <= job_pay_premise:
    # check if the estimate of 'job_pay_hypothesis' contradicts the actual value of 'job_pay_premise'
    label = "contradiction"
elif commission_hypothesis < 45000 * 0.45:
    # check if the estimated commission in the hypothesis contradicts the actual commission in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
