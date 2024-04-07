# Premise: Each week, James is paid x dollars per per hour for the first 40 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first more than 20 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: entailment

regular_hours_premise = 40
regular_hours_hypothesis = 20
overtime_rate_premise = 2
overtime_rate_hypothesis = 2

# the hypothesis refers to the number of regular hours and the pay rate for overtime hours,
# both of which are mentioned in the premise
if regular_hours_hypothesis > regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours in the premise
    label = "contradiction"
elif overtime_rate_hypothesis != overtime_rate_premise:
    # check if the overtime rate in the hypothesis contradicts the overtime rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

