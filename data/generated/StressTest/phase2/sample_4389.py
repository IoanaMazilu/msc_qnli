# Premise: Each week, Harry is paid x dollars per hour for the first 30 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first more than 20 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: entailment

standard_hours_premise = 30
standard_hours_hypothesis = 20
overtime_rate_premise = 1.5
overtime_rate_hypothesis = 1.5

# the hypothesis refers to the same pay structure in the premise, but the number of standard hours is different
if standard_hours_hypothesis >= standard_hours_premise:
    # check if the hypothesis value contradicts the number of standard hours in the premise
    label = "contradiction"
elif overtime_rate_hypothesis != overtime_rate_premise:
    # check if the rate for overtime pay in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones
    # but the hypothesis cannot be fully and directly inferred from the premise 
    label = "neutral"

print(label)

