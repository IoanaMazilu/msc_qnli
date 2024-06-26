matthew_wake_premise = "r"
matthew_wake_hypothesis = "y"
johnny_walk_premise = "y"
johnny_walk_hypothesis = "r"

# the hypothesis refers to the distance traveled by Johnny and the time elapsed
if johnny_walk_hypothesis!= johnny_walk_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif matthew_wake_hypothesis!= matthew_wake_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives only an estimate for the time elapsed and the distance traveled
    # any distance greater than '35 km' and any time elapsed consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
