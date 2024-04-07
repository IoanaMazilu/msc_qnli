# Premise: Faiza has 7 purses, she gives 3 purse as gift.
# Hypothesis: Faiza has less than 7 purses, she gives 3 purse as gift.
# Golden Label: contradiction

total_purses_premise = 7
given_purses_premise = 3
total_purses_hypothesis = 7
given_purses_hypothesis = 3

# the hypothesis refers to the number of total purses and given purses mentioned in the premise
if total_purses_hypothesis != total_purses_premise:
    # check if the total number of purses in the hypothesis contradicts the total number of purses reported in the premise
    label = "contradiction"
elif given_purses_hypothesis != given_purses_premise:
    # check if the number of given purses in the hypothesis contradicts the number of given purses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
