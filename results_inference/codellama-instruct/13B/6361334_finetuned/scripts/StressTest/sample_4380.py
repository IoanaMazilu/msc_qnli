hours_driven_premise = 1 + 3
hours_driven_hypothesis = 8

# the hypothesis refers to the total hours driven and the speed at which Andrew drove
if hours_driven_hypothesis >= hours_driven_premise:
    # check if the estimate of 'hours_driven_hypothesis' contradicts the total hours driven in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total hours driven
    # any number of hours driven less than 'hours_driven_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
