# Premise: Robert ate 7 chocolates, Nickel ate 3 chocolates.
# Hypothesis: Robert ate 1 chocolates, Nickel ate 3 chocolates.
# Golden Label: contradiction

robert_chocolates_premise = 7
nickel_chocolates_premise = 3
robert_chocolates_hypothesis = 1
nickel_chocolates_hypothesis = 3

# the hypothesis refers to the number of chocolates Robert and Nickel ate, mentioned in the premise
if robert_chocolates_hypothesis != robert_chocolates_premise:
    # check if the number of chocolates Robert ate in the hypothesis contradicts the number of chocolates Robert ate in the premise
    label = "contradiction"
elif nickel_chocolates_hypothesis != nickel_chocolates_premise:
    # check if the number of chocolates Nickel ate in the hypothesis contradicts the number of chocolates Nickel ate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

