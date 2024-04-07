# Premise: Each week, Harry is paid x dollars per hour for the first 35 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first more than 35 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: contradiction

regular_hours_premise = 35
regular_hours_hypothesis = 35

# the hypothesis refers to the number of regular hours mentioned in the premise
if regular_hours_hypothesis > regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours mentioned in the premise
    label = "contradiction"
else:
    # if the number of regular hours in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

