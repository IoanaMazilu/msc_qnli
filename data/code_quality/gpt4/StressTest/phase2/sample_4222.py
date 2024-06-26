total_hours_premise = 7
total_hours_hypothesis = 3

# the hypothesis refers to the total hours of jogging and walking stated in the premise
if total_hours_hypothesis >= total_hours_premise:
    # check if the total hours in the hypothesis contradicts the premise (less than 'total_hours_premise')
    label = "contradiction"
elif total_hours_hypothesis < total_hours_premise:
    # any number of hours less than 'total_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)