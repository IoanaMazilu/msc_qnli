# Premise: Each week, James is paid x dollars per per hour for the first 40 hours and 2 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first 50 hours and 2 x dollars for each additional hour worked that week.
# Golden Label: contradiction

standard_hours_premise = 40
standard_hours_hypothesis = 50

# the hypothesis refers to the same payment scheme as the premise, but with a different number of standard pay hours
if standard_hours_premise != standard_hours_hypothesis:
    # check if the number of standard pay hours in the hypothesis contradicts the number stated in the premise
    label = "contradiction"
else:
    # if the number of standard pay hours in the hypothesis matches the one in the premise, we can infer entailment
    label = "entailment"

print(label)

