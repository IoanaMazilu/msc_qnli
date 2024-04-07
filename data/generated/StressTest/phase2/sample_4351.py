# Premise: Vijay bought less than 660 shirts at the rate of Rs.
# Hypothesis: Vijay bought 160 shirts at the rate of Rs.
# Golden Label: neutral

shirts_bought_premise = 660
shirts_bought_hypothesis = 160

# the hypothesis talks about the number of shirts bought by Vijay, referenced also in the premise
if shirts_bought_hypothesis >= shirts_bought_premise:
    # check if the number of shirts bought in the hypothesis contradicts the estimate of less than 'shirts_bought_premise'
    label = "contradiction"
elif shirts_bought_hypothesis < shirts_bought_premise:
    # any number of shirts less than 'shirts_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

