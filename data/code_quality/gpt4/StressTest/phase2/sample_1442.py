max_work_hours_premise = 40

# the hypothesis suggests that Mary works more than the number of hours stated in the premise
if max_work_hours_premise >= max_work_hours_premise:
    # if the maximum work hours from the hypothesis are not more than those from the premise, then it's a contradiction
    label = "contradiction"
else:
    # the premise gives only a maximum limit for the work hours
    # any number of hours greater than 'max_work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
