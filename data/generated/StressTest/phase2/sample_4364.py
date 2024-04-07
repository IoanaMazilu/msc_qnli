# Premise: Each week, Harry is paid x dollars per hour for the first 18 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first more than 18 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: contradiction

# the unknown variable 'x' is the same for both the premise and hypothesis.
# 'x' is a constant factor in both the premise and hypothesis, so we can ignore it in our comparison.
standard_hours_premise = 18
standard_hours_hypothesis = 18

# the hypothesis refers to the number of standard hours of work per week mentioned in the premise
if standard_hours_hypothesis > standard_hours_premise:
    # check if the 'standard_hours_hypothesis' contradicts the number of standard hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

