fastest_horses_premise = 4
fastest_horses_hypothesis = 3
total_horses_premise = 25
total_horses_hypothesis = 25

# the hypothesis talks about the number of fastest horses to be submitted from London Racetrack, which is also referenced in the premise
if fastest_horses_hypothesis >= fastest_horses_premise:
    # check if the number of fastest horses in the hypothesis contradicts the number of fastest horses in the premise
    label = "contradiction"
elif fastest_horses_hypothesis < fastest_horses_premise:
    # if the number of fastest horses in the hypothesis is less than the number of fastest horses in the premise, it is entailed
    label = "entailment"
else:
    # if the number of fastest horses in the hypothesis does not contradict nor is less than the number of fastest horses in the premise, it is neutral
    label = "neutral"

print(label)
