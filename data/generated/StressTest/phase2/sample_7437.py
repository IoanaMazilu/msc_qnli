# Premise: The London Racetrack needs to submit its 3 fastest horses to the Kentucky Derby out of 25 horses.
# Hypothesis: The London Racetrack needs to submit its less than 4 fastest horses to the Kentucky Derby out of 25 horses.
# Golden Label: entailment

fastest_horses_premise = 3
fastest_horses_hypothesis = 4
total_horses_premise = 25
total_horses_hypothesis = 25

# the hypothesis refers to the number of fastest horses and total horses mentioned in the premise
if fastest_horses_hypothesis >= fastest_horses_premise:
    # check if the estimate of 'fastest_horses_hypothesis' contradicts the number of fastest horses needed in the premise
    label = "contradiction"
elif total_horses_hypothesis != total_horses_premise:
    # check if the total number of horses in the hypothesis contradicts the total number of horses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

