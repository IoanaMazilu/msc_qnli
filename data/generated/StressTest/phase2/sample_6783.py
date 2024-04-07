# Premise: Each week, James is paid x dollars per per hour for the first 40 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, James is paid x dollars per per hour for the first less than 70 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: entailment

# there is no explicit numerical value in this problem, but we can treat 'x' as a variable
x = 1  # it can be any positive number

# we use 40 and 70 as the standard hours per week mentioned in the premise and the hypothesis
standard_hours_premise = 40
standard_hours_hypothesis = 70

# the premise and the hypothesis refer to the hourly wage of James and the standard hours he works each week
if standard_hours_hypothesis <= standard_hours_premise:
    # check if the standard hours in the hypothesis contradict the standard hours in the premise
    label = "contradiction"
elif standard_hours_hypothesis > standard_hours_premise:
    # the hypothesis states that James is paid x dollars per hour for less than 70 hours which does not contradict the premise
    # but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

