# Premise: John left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus 15 percent commission.
# Hypothesis: John left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus 55 percent commission.
# Golden Label: contradiction

old_job_salary_premise = 75000
old_job_salary_hypothesis = 75000
new_job_salary_premise = 45000
new_job_salary_hypothesis = 45000
commission_premise = 15
commission_hypothesis = 55

# the hypothesis talks about John's old and new job salaries, and his commission, also mentioned in the premise
if old_job_salary_premise != old_job_salary_hypothesis:
    # check if the old job salary in the hypothesis contradicts the old job salary mentioned in the premise
    label = "contradiction"
elif new_job_salary_premise != new_job_salary_hypothesis:
    # check if the new job salary in the hypothesis contradicts the new job salary mentioned in the premise
    label = "contradiction"
elif commission_hypothesis < commission_premise:
    # check if the commission percentage in the hypothesis contradicts the commission percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives the exact value for the commission percentage
    # any commission percentage greater than 'commission_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

