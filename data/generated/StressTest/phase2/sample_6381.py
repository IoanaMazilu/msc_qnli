# Premise: Each week, James is paid x dollars per per hour for the first 40 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first less than 80 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: entailment

# This is a case where the values being compared are not explicit numbers, but variables. 
# The value of 'x' is not provided, but we can still reason about the relationships.

first_hours_premise = 40
additional_hours_premise = 2

first_hours_hypothesis = 80
additional_hours_hypothesis = 2

# The hypothesis refers to the amount James is paid per hour, as mentioned in the premise
if first_hours_hypothesis <= first_hours_premise:
    # check if the number of hours stated in the hypothesis contradicts the number stated in the premise
    label = "contradiction"
elif additional_hours_hypothesis != additional_hours_premise:
    # check if the rate of pay for additional hours in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

