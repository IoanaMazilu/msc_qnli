# Premise: Lucy has 212.0 fish and then she buys 280.0 more fish.
# Hypothesis: She has 492.0 fish now.
# Golden Label: entailment

fish_initial_premise = 212.0
fish_bought_premise = 280.0
fish_total_hypothesis = 492.0

# the hypothesis refers to the total number of fish, which are also mentioned in the premise
# compute the total number of fish in the premise
fish_total_premise = fish_initial_premise + fish_bought_premise

if fish_total_hypothesis != fish_total_premise:
    # check if the total number of fish in the hypothesis contradicts the total number of fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

