# Premise: Sally had 39.0 baseball cards and Sara gave Sally 24.0 more.
# Hypothesis: Sally has 64.0 baseball cards now.
# Golden Label: contradiction

initial_cards_sally_premise = 39.0
received_cards_sally_premise = 24.0
total_cards_sally_hypothesis = 64.0

# the hypothesis refers to the total number of baseball cards Sally has, which are also mentioned in the premise
# compute the total number of baseball cards Sally has in the premise
total_cards_sally_premise = initial_cards_sally_premise + received_cards_sally_premise
if total_cards_sally_hypothesis != total_cards_sally_premise:
    # check if the total number of baseball cards in the hypothesis contradicts the total number of baseball cards from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

