# Premise: Marcella has 20 pairs of shoes.
# Hypothesis: Marcella has 80 pairs of shoes.
# Golden Label: contradiction

shoes_premise = 20
shoes_hypothesis = 80

# the hypothesis talks about the number of pairs of shoes owned by Marcella, also mentioned in the premise
if shoes_hypothesis != shoes_premise:
    # check if the number of pairs of shoes in the hypothesis contradicts the number of pairs of shoes mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of shoes, and this number should be same as the number in the hypothesis for entailment
    label = "entailment"

print(label)

