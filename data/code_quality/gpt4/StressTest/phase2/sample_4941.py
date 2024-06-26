shift_hours_premise = 8
shifts_premise = 3
orders_per_hour_premise = 40

shift_hours_hypothesis = 4
shifts_hypothesis = 3
orders_per_hour_hypothesis = 40

# the hypothesis talks about the number of shifts and orders per hour, referenced also in the premise
if shifts_premise != shifts_hypothesis or orders_per_hour_hypothesis != orders_per_hour_premise:
    # check if the hypothesis values contradict the premise values for shifts and orders per hour
    label = "contradiction"
elif shift_hours_premise <= shift_hours_hypothesis:
    # check if the hypothesis value for shift hours contradicts the premise value
    label = "contradiction"
else:
    # the premise gives exact values for the number of shifts, shift hours, and orders per hour
    # any number of hours greater than 'shift_hours_hypothesis' and equal to the other values does not contradict the premise
    # but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
