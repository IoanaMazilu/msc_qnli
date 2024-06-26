premise_speed = 1
premise_time = 3
hypothesis_speed = 2
hypothesis_time = 3

# the hypothesis refers to the speed of Anne and the time it takes to clean the house
if hypothesis_speed * hypothesis_time < premise_speed * premise_time:
    # check if the estimate of 'hypothesis_time' contradicts the time in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes to clean the house
    # any time less than 'premise_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
