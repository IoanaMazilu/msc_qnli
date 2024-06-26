job_pay_premise = 150
job_pay_hypothesis = 150

# the hypothesis refers to the pay of Lexi's job, which is also mentioned in the premise
if job_pay_hypothesis >= job_pay_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif job_pay_hypothesis < job_pay_premise:
    # if the hypothesis value is less than the premise value, it can be entailed from the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
