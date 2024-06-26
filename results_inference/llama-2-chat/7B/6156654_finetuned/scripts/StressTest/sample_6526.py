# the premise and hypothesis are about the on-time departure rate of flights from Phoenix Airport
# the premise gives the rate as less than 20%
# the hypothesis gives the rate as more than 60%

# compute the on-time departure rate from the premise
rate_premise = 20

# compute the on-time departure rate from the hypothesis
rate_hypothesis = 60

# check if the hypothesis rate contradicts the premise rate
if rate_hypothesis <= rate_premise:
    label = "contradiction"
elif rate_hypothesis > rate_premise:
    # check if the hypothesis rate entails the premise rate
    if rate_hypothesis - rate_premise >= 0:
        label = "entailment"
    else:
        label = "neutral"

print(label)
