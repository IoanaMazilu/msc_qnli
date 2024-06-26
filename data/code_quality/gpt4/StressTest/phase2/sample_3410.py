shift_duration_premise = 8
shift_duration_hypothesis = 2
shifts_per_week_premise = 5
shifts_per_week_hypothesis = 5
orders_per_hour_premise = 40
orders_per_hour_hypothesis = 40

# the hypothesis refers to the work shifts and the average orders per hour mentioned in the premise
if shifts_per_week_hypothesis != shifts_per_week_premise:
    # check if the number of work shifts in the hypothesis contradicts the number of work shifts reported in the premise
    label = "contradiction"
elif shift_duration_hypothesis > shift_duration_premise:
    # check if the duration of the work shifts in the hypothesis contradicts the durations reported in the premise
    label = "contradiction"
elif orders_per_hour_hypothesis != orders_per_hour_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
