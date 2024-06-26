job_pay_premise = 75000
job_pay_hypothesis = 75000
sales_job_pay_premise = 45000
sales_job_pay_hypothesis = 45000
commission_premise = 15
commission_hypothesis = 55

# the hypothesis talks about the same job and salary as the premise
if job_pay_hypothesis!= job_pay_premise:
    # check if the salary in the hypothesis contradicts the salary in the premise
    label = "contradiction"
elif sales_job_pay_hypothesis!= sales_job_pay_premise:
    # check if the salary in the hypothesis contradicts the salary in the premise
    label = "contradiction"
elif commission_hypothesis!= commission_premise:
    # check if the commission in the hypothesis contradicts the commission in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
