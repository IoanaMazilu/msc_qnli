fast_horses_premise = 3
total_horses_premise = 25
fast_horses_hypothesis = 4
total_horses_hypothesis = 25

# the hypothesis talks about the number of fastest horses that the London Racetrack needs to submit to the Kentucky Derby, which is also mentioned in the premise
# it also refers to the total number of horses in the London Racetrack, which is the same in the premise
if fast_horses_hypothesis != fast_horses_premise:
    # check if the number of fastest horses in the hypothesis contradicts the number of fastest horses in the premise
    label = "contradiction"
elif total_horses_hypothesis != total_horses_premise:
    # check if the total number of horses in the hypothesis contradicts the total number of horses in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
