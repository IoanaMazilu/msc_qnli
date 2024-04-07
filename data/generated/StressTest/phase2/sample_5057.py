# Premise: All of them started to work together but Rashmi leaves after 4 days.
# Hypothesis: All of them started to work together but Rashmi leaves after less than 4 days.
# Golden Label: contradiction

rashmi_work_days_premise = 4
rashmi_work_days_hypothesis = 4

# the hypothesis refers to the number of days Rashmi worked, also mentioned in the premise
if rashmi_work_days_hypothesis < rashmi_work_days_premise:
    # check if the hypothesis value contradicts the number of work days in the premise
    label = "contradiction"
elif rashmi_work_days_hypothesis > rashmi_work_days_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

