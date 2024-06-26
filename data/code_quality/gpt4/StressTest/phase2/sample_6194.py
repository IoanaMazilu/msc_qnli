job_pay_premise = 150
job_pay_hypothesis = 150

# the hypothesis refers to the pay of Lexi's new job mentioned in the premise
if job_pay_hypothesis >= job_pay_premise:
    # check if the hypothesis value contradicts the pay in the premise
    label = "contradiction"
else:
    # if the hypothesis pay does not contradict the premise pay, we can infer entailment
    label = "entailment"

print(label)
