# Premise: Suresh works for 9 hours and then the remaining job is completed by Ashutosh.
# Hypothesis: Suresh works for more than 6 hours and then the remaining job is completed by Ashutosh.
# Golden Label: entailment

work_hours_suresh_premise = 9
work_hours_suresh_hypothesis = 6

# the hypothesis refers to the number of working hours of Suresh mentioned in the premise
if work_hours_suresh_premise < work_hours_suresh_hypothesis:
    # check if the estimate of 'work_hours_suresh_hypothesis' contradicts the number of working hours in the premise
    label = "contradiction"
elif work_hours_suresh_premise == work_hours_suresh_hypothesis:
    # check if the number of working hours in the hypothesis equals the number of working hours reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

