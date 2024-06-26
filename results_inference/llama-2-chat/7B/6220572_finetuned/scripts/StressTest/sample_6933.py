job_pay_premise = 75000
job_pay_hypothesis = 75000
commission_rate_hypothesis = 0.45

# the hypothesis talks about the job pay and commission rate, referenced also in the premise
if job_pay_hypothesis!= job_pay_premise:
    # check if the job pay in the hypothesis contradicts the job pay reported in the premise
    label = "contradiction"
elif commission_rate_hypothesis >= 0.45:
    # check if the commission rate in the hypothesis contradicts the estimate of less than 0.45 commission rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
