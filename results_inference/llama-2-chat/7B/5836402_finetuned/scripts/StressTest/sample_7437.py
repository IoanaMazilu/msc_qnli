fastest_horses_premise = 3
fastest_horses_hypothesis = 4
total_horses_premise = 25
total_horses_hypothesis = 25

# the hypothesis refers to the number of fastest horses that need to be submitted by the London Racetrack
if fastest_horses_hypothesis >= fastest_horses_premise:
    # check if the hypothesis value contradicts the number of fastest horses needed in the premise
    label = "contradiction"
elif fastest_horses_hypothesis < fastest_horses_premise:
    # check if the number of fastest horses in the hypothesis is less than the number of fastest horses needed in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
