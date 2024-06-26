rashmi_work_days_premise = 4
rashmi_work_days_hypothesis = 8

# the hypothesis talks about the number of days Rashmi worked, referenced also in the premise
if rashmi_work_days_hypothesis < rashmi_work_days_premise:
    # check if the hypothesis value contradicts the exact number of 'rashmi_work_days_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of days Rashmi worked
    # any number of days less than or equal to 'rashmi_work_days_premise' can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)
