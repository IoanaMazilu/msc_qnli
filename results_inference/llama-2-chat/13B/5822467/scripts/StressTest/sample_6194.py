lexi_job_premise = 150
lexi_job_hypothesis = 100

# the hypothesis refers to the amount of money Lexi earns per day
if lexi_job_hypothesis <= lexi_job_premise:
    # check if the hypothesis value contradicts the estimate of $150 per day in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money Lexi earns per day
    # any amount less than $150 per day is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
