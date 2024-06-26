number_jobs_premise = 533000
number_jobs_hypothesis = 533000
years_premise = 34
years_hypothesis = 34

# the hypothesis and premise mention the number of jobs lost in November and the number of years since the last time this number was reached
if number_jobs_premise!= number_jobs_hypothesis:
    # check if the number of jobs lost in the hypothesis contradicts the number of jobs lost in the premise
    label = "contradiction"
elif years_hypothesis < years_premise:
    # check if the estimated number of years since the last time this number was reached in the hypothesis contradicts the premise estimate of more than 'years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years since the last time this number was reached
    # any estimate of the number of years in the hypothesis greater or equal to 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
