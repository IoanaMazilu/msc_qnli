shift_hours_premise = 36
shift_hours_hypothesis = 16
average_orders_per_hour = 40

# the hypothesis talks about the number of hours Jill worked this week, referenced also in the premise
if shift_hours_hypothesis > shift_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than'shift_hours_premise'
    label = "contradiction"
elif shift_hours_hypothesis < shift_hours_premise:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than'shift_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
