travel_hours_premise = 70
travel_hours_hypothesis = 20

# the hypothesis refers to the number of hours Bhavan travelled which is also mentioned in the premise
if travel_hours_hypothesis >= travel_hours_premise:
    # check if the number of hours Bhavan travelled in the hypothesis contradicts the upper bound given in the premise
    label = "contradiction"
else:
    # the premise gives only an upper bound for the number of hours Bhavan travelled
    # any number of less than 'travel_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
