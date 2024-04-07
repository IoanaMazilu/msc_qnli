# Premise: Mike buys 3 cartons of eggs at the store.
# Hypothesis: Mike buys 2 cartons of eggs at the store.
# Golden Label: contradiction

cartons_eggs_premise = 3
cartons_eggs_hypothesis = 2

# the hypothesis talks about the number of egg cartons Mike buys, referenced also in the premise
if cartons_eggs_hypothesis != cartons_eggs_premise:
    # check if the number of egg cartons in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

