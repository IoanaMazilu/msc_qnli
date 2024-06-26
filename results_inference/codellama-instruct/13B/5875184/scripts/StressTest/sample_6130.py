premise_hours_per_week = 11
premise_dollars_per_hour = x
premise_additional_hours = 1.5

hypothesis_hours_per_week = 21
hypothesis_dollars_per_hour = x
hypothesis_additional_hours = 1.5

# check if the premise hours per week is less than the hypothesis hours per week
if premise_hours_per_week < hypothesis_hours_per_week:
    # check if the premise dollars per hour is less than the hypothesis dollars per hour
    if premise_dollars_per_hour < hypothesis_dollars_per_hour:
        # check if the premise additional hours is less than the hypothesis additional hours
        if premise_additional_hours < hypothesis_additional_hours:
            # the hypothesis is more specific than the premise, so it entails the premise
            label = "entailment"
        else:
            # the premise is more specific than the hypothesis, so it contradicts the hypothesis
            label = "contradiction"
    else:
        # the premise dollars per hour is not less than the hypothesis dollars per hour, so it is neutral
        label = "neutral"
else:
    # the premise hours per week is not less than the hypothesis hours per week, so it is neutral
    label = "neutral"

print(label)
