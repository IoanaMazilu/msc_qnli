# Premise: Marcella has 20 pairs of shoes.
# Hypothesis: Marcella has more than 10 pairs of shoes.
# Golden Label: entailment

pairs_of_shoes_premise = 20
pairs_of_shoes_hypothesis = 10

# the hypothesis talks about the quantity of pairs of shoes Marcella has, mentioned also in the premise
if pairs_of_shoes_premise <= pairs_of_shoes_hypothesis:
    # check if the total number of pairs of shoes in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # if the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)

