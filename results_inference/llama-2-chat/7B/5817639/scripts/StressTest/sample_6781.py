x_per_hour_premise = float(input("Premise: x per hour"))
x_per_hour_hypothesis = float(input("Hypothesis: x per hour"))

# the hypothesis talks about the hourly wage for Harry, referenced also in the premise
if x_per_hour_hypothesis <= x_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of 'x_per_hour_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the hourly wage
    # any hourly wage greater than 'x_per_hour_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
