# Premise: Jerry left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus 15 percent commission.
# Hypothesis: Jerry left a job paying $75,000 per year to accept a sales job paying $45,000 per year plus less than 45 percent commission.
# Golden Label: entailment

old_salary_premise = 75000
old_salary_hypothesis = 75000
new_salary_premise = 45000
new_salary_hypothesis = 45000
commission_premise = 15
commission_hypothesis = 45

# the hypothesis talks about Jerry's old salary, new salary and commission percentage
if old_salary_hypothesis != old_salary_premise:
    # check if the old salary in the hypothesis contradicts the old salary mentioned in the premise
    label = "contradiction"
elif new_salary_hypothesis != new_salary_premise:
    # check if the new salary in the hypothesis contradicts the new salary mentioned in the premise
    label = "contradiction"
elif commission_hypothesis <= commission_premise:
    # check if the commission percentage in the hypothesis contradicts the commission percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

