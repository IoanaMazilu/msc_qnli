matthew_wake_premise = "t"
matthew_wake_hypothesis = "y"
johnny_walk_premise = "y"
johnny_walk_hypothesis = "t"

# the hypothesis refers to the distance traveled by Johnny and the time elapsed since Matthew woke up
if johnny_walk_hypothesis!= johnny_walk_premise:
    # check if the hypothesis value contradicts the value of Johnny's starting point in the premise
    label = "contradiction"
elif matthew_wake_hypothesis!= matthew_wake_premise:
    # check if the hypothesis value contradicts the value of Matthew's starting point in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled by Johnny and the time elapsed since Matthew woke up
    # any distance greater than '35 km' and any time elapsed since Matthew woke up is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
