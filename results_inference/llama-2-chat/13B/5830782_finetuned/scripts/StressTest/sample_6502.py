matthew_rate_premise = 5
matthew_rate_hypothesis = 3
johnny_rate_premise = 4
johnny_rate_hypothesis = 4

# the hypothesis refers to the walking rates of Matthew and Johnny, mentioned in the premise
if matthew_rate_hypothesis >= matthew_rate_premise:
    # check if the value of'matthew_rate_hypothesis' contradicts the estimate of less than'matthew_rate_premise'
    label = "contradiction"
elif johnny_rate_hypothesis!= johnny_rate_premise:
    # check if the value of 'johnny_rate_hypothesis' contradicts the value of 'johnny_rate_premise'
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but they cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
