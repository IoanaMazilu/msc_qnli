# Premise: The watch store down the street from Wendy's house has 2 leather watches, 1 gold watch, and 1 silver watch.
# Hypothesis: The watch store down the street from Wendy's house has more than 2 leather watches, 1 gold watch, and 1 silver watch.
# Golden Label: contradiction

leather_watches_premise = 2
leather_watches_hypothesis = 2
gold_watches_premise = 1
gold_watches_hypothesis = 1
silver_watches_premise = 1
silver_watches_hypothesis = 1

# the hypothesis refers to the number of each type of watch mentioned in the premise
if leather_watches_hypothesis > leather_watches_premise:
    # check if the number of leather watches in the hypothesis contradicts the number of leather watches reported in the premise
    label = "contradiction"
elif gold_watches_hypothesis != gold_watches_premise or silver_watches_hypothesis != silver_watches_premise:
    # check if the number of gold or silver watches in the hypothesis contradicts the number of gold or silver watches reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

