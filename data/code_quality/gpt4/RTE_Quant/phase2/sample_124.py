govt_casualties_premise = 11
rebel_casualties_premise = 3
rebel_casualties_hypothesis = 3

# the hypothesis talks about the number of rebel casualties caused by the government troops, which is also mentioned in the premise
if rebel_casualties_hypothesis != rebel_casualties_premise:
    # check if the number of rebel casualties in the hypothesis contradicts the number of rebel casualties from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
