# Premise: Each week, Harry is paid x dollars per hour for the first 30 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first 80 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: contradiction

hours_paid_normal_rate_premise = 30
hours_paid_double_rate_premise = None
hours_paid_normal_rate_hypothesis = 80
hours_paid_double_rate_hypothesis = None

# the hypothesis refers to the number of hours Harry is paid a normal and double rate for, mentioned in the premise
if hours_paid_normal_rate_hypothesis != hours_paid_normal_rate_premise:
    # check if the number of hours paid at a normal rate in the hypothesis contradicts the number of hours paid at a normal rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

