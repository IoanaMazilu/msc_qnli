day_of_week_premise = ["Monday", "Wednesday", "Friday"]
day_of_week_hypothesis = ["Monday", "Wednesday", "Friday"]

# the hypothesis refers to the days of the week that Mary works, as stated in the premise
if any(day in day_of_week_hypothesis for day in day_of_week_premise):
    # check if the estimate of 'day_of_week_hypothesis' contradicts the day of the week reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the days of the week that Mary works
    # any day of the week that Mary works is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
