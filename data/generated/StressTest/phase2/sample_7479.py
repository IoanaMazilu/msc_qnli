# Premise: Each week, Harry is paid x dollars per hour for the first 24 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first less than 84 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: entailment

hours_worked_regular_premise = 24
hours_worked_regular_hypothesis = 84

# The hypothesis describes the number of hours Harry is paid x dollars, referenced also in the premise
if hours_worked_regular_hypothesis > hours_worked_regular_premise:
    # Check if the hypothesis value contradicts the premise value for hours worked at x dollars
    label = "contradiction"
else:
    # Any number of hours less than or equal to 'hours_worked_regular_premise' is consistent with the premise
    label = "neutral"

print(label)

