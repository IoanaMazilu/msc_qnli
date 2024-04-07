# Premise: He successfully married his girlfriend Diana after 1/7 more of his life.
# Hypothesis: He successfully married his girlfriend Diana after more than 1/7 more of his life.
# Golden Label: contradiction

life_premise = 1/7
life_hypothesis = 1/7

# the hypothesis refers to the fraction of his life after which he married Diana, as mentioned in the premise
if life_hypothesis <= life_premise:
    # check if the fraction of his life in the hypothesis contradicts the fraction of his life mentioned in the premise
    label = "contradiction"
else:
    # if the fraction of his life in the hypothesis does not contradict the fraction of his life in the premise, we can infer entailment
    label = "entailment"

print(label)

