job_pay_premise = 75000
job_pay_hypothesis = 75000
commission_premise = 35
commission_hypothesis = 15

# the hypothesis talks about the same job and commission as the premise, but with a different commission percentage
if job_pay_hypothesis!= job_pay_premise:
    # check if the job pay in the hypothesis contradicts the job pay in the premise
    label = "contradiction"
elif commission_hypothesis!= commission_premise:
    # check if the commission percentage in the hypothesis contradicts the commission percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and percentages do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
