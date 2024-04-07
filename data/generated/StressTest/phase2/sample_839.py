# Premise: Vijay bought 160 shirts at the rate of Rs.
# Hypothesis: Vijay bought 860 shirts at the rate of Rs.
# Golden Label: contradiction

shirts_bought_premise = 160
shirts_bought_hypothesis = 860

# the hypothesis talks about the number of shirts Vijay bought, which is also mentioned in the premise
if shirts_bought_hypothesis != shirts_bought_premise:
    # check if the number of shirts in the hypothesis contradicts the number of shirts mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

