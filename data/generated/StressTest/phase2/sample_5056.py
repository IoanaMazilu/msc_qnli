# Premise: All of them started to work together but Rashmi leaves after less than 8 days.
# Hypothesis: All of them started to work together but Rashmi leaves after 4 days.
# Golden Label: neutral

rashmi_work_days_premise = 8
rashmi_work_days_hypothesis = 4

# the hypothesis talks about the number of days Rashmi worked, which is also referenced in the premise
if rashmi_work_days_hypothesis >= rashmi_work_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rashmi_work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Rashmi worked
    # any number of days less than 'rashmi_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

