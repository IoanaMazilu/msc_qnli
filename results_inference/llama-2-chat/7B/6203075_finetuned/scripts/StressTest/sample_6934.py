job_pay_premise = 75000
job_pay_hypothesis = 75000
job_pay_hypothesis_commission = 15

# the hypothesis talks about the same job and commission as the premise
if job_pay_hypothesis!= job_pay_premise:
    # check if the job pay in the hypothesis contradicts the job pay in the premise
    label = "contradiction"
elif job_pay_hypothesis_commission!= 45:
    # check if the commission percentage in the hypothesis contradicts the commission percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
