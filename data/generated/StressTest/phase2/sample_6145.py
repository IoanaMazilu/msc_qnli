# Premise: Each week, Harry is paid x dollars per hour for the first less than 75 hours and 1.5 x dollars for each additional hour worked that week.
# Hypothesis: Each week, Harry is paid x dollars per hour for the first 35 hours and 1.5 x dollars for each additional hour worked that week.
# Golden Label: neutral

regular_hours_premise = 75
regular_hours_hypothesis = 35

# the hypothesis refers to the number of regular paid hours mentioned in the premise
if regular_hours_hypothesis >= regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours in the premise
    label = "contradiction"
elif regular_hours_hypothesis < regular_hours_premise:
    # if the number of regular hours in the hypothesis is less than the number of regular hours in the premise,
    # it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

