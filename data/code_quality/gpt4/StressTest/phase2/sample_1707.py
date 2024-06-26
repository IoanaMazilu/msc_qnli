shifts_premise = 9
shifts_hypothesis = 7
hours_per_shift = 4
earn_per_hour = 40

# the hypothesis talks about the number of shifts and earning per hour, referenced also in the premise
if shifts_premise < hours_per_shift + shifts_hypothesis:
    # check if the hypothesis value contradicts the number of shifts worked in the premise
    label = "contradiction"
elif earn_per_hour != earn_per_hour:
    # check if the earning per hour in the hypothesis contradicts the earning per hour in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
