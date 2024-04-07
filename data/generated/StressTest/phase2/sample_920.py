# Premise: He gave 19 toys to his brother Gourav, while Gourav playing all but 6 got destroyed.
# Hypothesis: He gave less than 19 toys to his brother Gourav, while Gourav playing all but 6 got destroyed.
# Golden Label: contradiction

toys_given_premise = 19
toys_given_hypothesis = 19
toys_left_premise = 6
toys_left_hypothesis = 6

# the hypothesis refers to the number of toys given to Gourav and the number of toys left after playing
if toys_given_hypothesis >= toys_given_premise:
    # check if the estimate of 'toys_given_hypothesis' contradicts the number of toys given in the premise
    label = "contradiction"
elif toys_left_hypothesis != toys_left_premise:
    # check if the number of toys left in the hypothesis contradicts the number of toys left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

