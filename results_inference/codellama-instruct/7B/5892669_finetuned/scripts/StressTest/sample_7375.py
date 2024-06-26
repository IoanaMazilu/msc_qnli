shifts_hours_premise = 36
shifts_hours_hypothesis = 16
average_orders_hour_premise = 40
average_orders_hour_hypothesis = 40

# the hypothesis refers to the number of hours of work and the average orders per hour mentioned in the premise
if shifts_hours_hypothesis >= shifts_hours_premise:
    # check if the number of hours of work in the hypothesis contradicts the estimate of less than'shifts_hours_premise'
    label = "contradiction"
elif average_orders_hour_hypothesis!= average_orders_hour_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours of work
    # any number of hours less than'shifts_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
