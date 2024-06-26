job_pay_premise = 75000
job_pay_hypothesis = 75000
new_job_pay_premise = 45000
new_job_pay_hypothesis = 45000
commission_premise = 35
commission_hypothesis = 15

# the hypothesis talks about the same job and salary as the premise, but with different commission percentage
if commission_hypothesis!= commission_premise:
    label = "contradiction"
elif new_job_pay_hypothesis!= new_job_pay_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
