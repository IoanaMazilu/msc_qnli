fastest_horses_premise = 3
fastest_horses_hypothesis = 4

# the hypothesis refers to the number of fastest horses to be submitted from the London Racetrack to the Kentucky Derby
if fastest_horses_hypothesis == fastest_horses_premise:
    # check if the number of fastest horses in the hypothesis contradicts the number of fastest horses in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
