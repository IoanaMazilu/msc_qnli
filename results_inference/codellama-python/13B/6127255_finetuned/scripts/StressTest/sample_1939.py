john_raking_time_premise = 60
john_raking_time_hypothesis = 30
todd_raking_time_premise = 60
todd_raking_time_hypothesis = 60

# the hypothesis refers to the time it takes John and Todd to rake a lawn, as mentioned in the premise
if john_raking_time_hypothesis >= john_raking_time_premise:
    # check if the time it takes John to rake a lawn in the hypothesis contradicts the premise
    label = "contradiction"
elif todd_raking_time_hypothesis!= todd_raking_time_premise:
    # check if the time it takes Todd to rake a lawn in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes John to rake a lawn
    # the exact time 'john_raking_time_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
