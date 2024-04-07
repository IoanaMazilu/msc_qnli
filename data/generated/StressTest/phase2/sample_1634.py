# Premise: Vijay bought 160 shirts at the rate of Rs.
# Hypothesis: Vijay bought more than 160 shirts at the rate of Rs.
# Golden Label: contradiction

shirts_bought_premise = 160
shirts_bought_hypothesis = 160

# the hypothesis talks about the number of shirts bought by Vijay, referenced also in the premise
if shirts_bought_hypothesis <= shirts_bought_premise:
    # check if the hypothesis estimate contradicts the number of shirts bought in the premise
    label = "entailment"
else:
    # the premise gives an exact number for the shirts bought by Vijay
    # any number of shirts greater than 'shirts_bought_premise' contradicts the premise
    label = "contradiction"

print(label)

