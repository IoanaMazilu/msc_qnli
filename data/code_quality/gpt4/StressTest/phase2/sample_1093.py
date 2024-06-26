first_speed_premise = 20
first_speed_hypothesis = 30
second_speed_premise = 15
second_speed_hypothesis = 15

# the hypothesis refers to the speed Susan drove during the first and second part of her trip, mentioned in the premise
if first_speed_hypothesis <= first_speed_premise:
    # check if the estimate of 'first_speed_hypothesis' contradicts the number of first part speed in the premise
    label = "contradiction"
elif second_speed_hypothesis != second_speed_premise:
    # check if the speed of second part in the hypothesis contradicts the speed of second part reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of first part
    # any speed greater than 'first_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
