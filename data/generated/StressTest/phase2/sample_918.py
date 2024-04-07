# Premise: He gave 19 toys to his brother Gourav, while Gourav playing all but 6 got destroyed.
# Hypothesis: He gave less than 89 toys to his brother Gourav, while Gourav playing all but 6 got destroyed.
# Golden Label: entailment

toys_given_premise = 19
toys_given_hypothesis = 89
toys_left = 6

# the hypothesis talks about the number of toys given and the number of toys left after playing, both referenced also in the premise
if toys_given_premise >= toys_given_hypothesis:
    # check if the hypothesis value contradicts the number of toys given in the premise
    label = "contradiction"
elif toys_left != 6:
    # check if the number of toys left in the hypothesis contradicts the number of toys left reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

