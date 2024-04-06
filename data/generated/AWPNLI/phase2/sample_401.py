# Premise: Mike has 87.0 baseball cards and Sam gave Mike 13.0 more baseball cards.
# Hypothesis: Mike has 96.0 baseball cards now.
# Golden Label: contradiction

mike_baseball_cards_premise = 87.0
sam_gave_baseball_cards_premise = 13.0
total_baseball_cards_hypothesis = 96.0

# the hypothesis refers to the total number of baseball cards Mike has now, which can be computed from the premise
# compute the total number of baseball cards in the premise
total_baseball_cards_premise = mike_baseball_cards_premise + sam_gave_baseball_cards_premise
if total_baseball_cards_hypothesis != total_baseball_cards_premise:
    # check if the total number of baseball cards in the hypothesis contradicts the total number of baseball cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

