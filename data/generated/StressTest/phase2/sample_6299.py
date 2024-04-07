# Premise: Each week, Harry is paid x dollars per hour for the first 12 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first 52 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: contradiction

first_hours_worked_premise = 12
first_hours_worked_hypothesis = 52

# the hypothesis refers to the number of hours worked per week mentioned in the premise
if first_hours_worked_hypothesis != first_hours_worked_premise:
    # check if the number of first hours worked in the hypothesis contradicts the number of first hours worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

