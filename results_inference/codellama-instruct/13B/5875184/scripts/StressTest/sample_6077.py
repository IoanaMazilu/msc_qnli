premise = "It takes John exactly 30 minutes to rake a lawn and it takes his son Todd exactly 60 minutes to rake the same lawn."
hypothesis = "It takes John exactly more than 30 minutes to rake a lawn and it takes his son Todd exactly 60 minutes to rake the same lawn."

# extract the numerical entities from the premise
minutes_john = 30
minutes_todd = 60

# extract the numerical entities from the hypothesis
minutes_john_hypothesis = 30
minutes_todd_hypothesis = 60

# check if the hypothesis values contradict the premise values
if minutes_john_hypothesis <= minutes_john:
    label = "contradiction"
elif minutes_todd_hypothesis!= minutes_todd:
    label = "contradiction"
else:
    label = "neutral"

print(label)
