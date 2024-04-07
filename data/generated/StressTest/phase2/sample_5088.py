# Premise: When Sally went to the candy store, she bought 25 licorice sticks.
# Hypothesis: When Sally went to the candy store, she bought less than 45 licorice sticks.
# Golden Label: entailment

licorice_sticks_premise = 25
licorice_sticks_hypothesis = 45

# the hypothesis refers to the number of licorice sticks bought by Sally, mentioned in the premise
if licorice_sticks_premise >= licorice_sticks_hypothesis:
    # check if the number of licorice sticks bought in the premise contradicts the estimate of less than 'licorice_sticks_hypothesis'
    label = "contradiction"
else:
    # if the premise value is less than the hypothesis value, we can infer entailment
    label = "entailment"

print(label)

