# Premise: Suresh works for 9 hours and then the remaining job is completed by Ashutosh.
# Hypothesis: Suresh works for 6 hours and then the remaining job is completed by Ashutosh.
# Golden Label: contradiction

suresh_work_hours_premise = 9
suresh_work_hours_hypothesis = 6

# the hypothesis refers to the working hours of Suresh mentioned in the premise
if suresh_work_hours_hypothesis > suresh_work_hours_premise:
    # check if the number of working hours in the hypothesis contradicts the number of working hours reported in the premise
    label = "contradiction"
elif suresh_work_hours_hypothesis < suresh_work_hours_premise:
    # check if the number of working hours in the hypothesis contradicts the number of working hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

