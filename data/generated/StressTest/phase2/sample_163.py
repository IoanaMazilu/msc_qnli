# Premise: He works at it for less than 30 days and then Rajesh finished it in 30 days.
# Hypothesis: He works at it for 20 days and then Rajesh finished it in 30 days.
# Golden Label: neutral

work_duration_premise = 30
work_duration_hypothesis = 20
rajesh_work_duration_premise = 30
rajesh_work_duration_hypothesis = 30

# the hypothesis references the work duration of 'he' and Rajesh mentioned in the premise
if work_duration_hypothesis >= work_duration_premise:
    # check if the work duration in the hypothesis contradicts the estimate of less than 'work_duration_premise' days
    label = "contradiction"
elif rajesh_work_duration_hypothesis != rajesh_work_duration_premise:
    # check if Rajesh's work duration in the hypothesis contradicts Rajesh's work duration reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

