# Premise: Only about 50 of the cards -- handed out over-the-counter at its offices -- had the error, it said.
# Hypothesis: About 50 of the incorrect cards were handed out, Maricopa County says.
# Golden Label: entailment

cards_error_premise = 50
cards_error_hypothesis = 50

# the hypothesis mentions the number of incorrect cards that were handed out, which is also referenced in the premise
if cards_error_hypothesis != cards_error_premise:
    # check if the number of incorrect cards in the hypothesis contradicts the number of incorrect cards reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

