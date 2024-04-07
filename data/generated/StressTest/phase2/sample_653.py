# Premise: Ben left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus 15 percent commission.
# Hypothesis: Ben left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus 85 percent commission.
# Golden Label: contradiction

old_job_salary_premise = 75000
new_job_salary_premise = 45000
commission_premise = 15

old_job_salary_hypothesis = 75000
new_job_salary_hypothesis = 45000
commission_hypothesis = 85

# The hypothesis talks about the same salaries and commissions mentioned in the premise
if old_job_salary_hypothesis != old_job_salary_premise:
    # check if the old job salary in the hypothesis contradicts the old job salary in the premise
    label = "contradiction"
elif new_job_salary_hypothesis != new_job_salary_premise:
    # check if the new job salary in the hypothesis contradicts the new job salary in the premise
    label = "contradiction"
elif commission_hypothesis < commission_premise:
    # check if the commission in the hypothesis is less than the commission in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the premise ones, but the commission in the hypothesis is higher than the one in the premise
    # we cannot explicitly entail the higher commission from the premise, hence the label is neutral
    label = "neutral"

print(label)

