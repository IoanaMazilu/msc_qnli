# Premise: Vijay bought 160 shirts at the rate of Rs.
# Hypothesis: Vijay bought less than 760 shirts at the rate of Rs.
# Golden Label: entailment

shirts_bought_premise = 160
shirts_bought_hypothesis = 760

# the hypothesis talks about the number of shirts Vijay bought, referenced also in the premise
if shirts_bought_hypothesis <= shirts_bought_premise:
    # check if the hypothesis value contradicts the exact number of 'shirts_bought_premise'
    label = "contradiction"
elif shirts_bought_premise >= shirts_bought_hypothesis:
    # check if the number of shirts bought in the premise contradicts the less than 'shirts_bought_hypothesis' estimate
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

