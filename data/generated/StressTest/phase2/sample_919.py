# Premise: He gave less than 89 toys to his brother Gourav, while Gourav playing all but 6 got destroyed.
# Hypothesis: He gave 19 toys to his brother Gourav, while Gourav playing all but 6 got destroyed.
# Golden Label: neutral

toys_given_premise = 89
toys_given_hypothesis = 19
toys_left_premise = 6
toys_left_hypothesis = 6

# the hypothesis refers to the number of toys given to Gourav and the number of toys left after Gourav played with them, both mentioned in the premise
if toys_given_hypothesis >= toys_given_premise:
    # check if the number of toys given in the hypothesis contradicts the estimate of less than 'toys_given_premise' in the premise
    label = "contradiction"
elif toys_left_hypothesis != toys_left_premise:
    # check if the number of toys left after Gourav played with them in the hypothesis contradicts the number of toys left in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

