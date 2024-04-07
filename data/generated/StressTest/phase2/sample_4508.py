# Premise: Each week, James is paid x dollars per per hour for the first 40 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first 60 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: contradiction

normal_hours_premise = 40
normal_hours_hypothesis = 60
overtime_rate_premise = 2
overtime_rate_hypothesis = 2

# the hypothesis refers to James' pay rate, as does the premise
if normal_hours_hypothesis != normal_hours_premise:
    # check if the number of normal hours worked per week in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif overtime_rate_hypothesis != overtime_rate_premise:
    # check if the rate for overtime hours in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

