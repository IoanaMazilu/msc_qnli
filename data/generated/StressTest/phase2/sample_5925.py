# Premise: Faiza has 14 purses, she gives 3 purse as gift.
# Hypothesis: Faiza has less than 34 purses, she gives 3 purse as gift.
# Golden Label: entailment

total_purses_premise = 14
gift_purses_premise = 3
total_purses_hypothesis = 34
gift_purses_hypothesis = 3

# the hypothesis refers to the number of total purses and gift purses mentioned in the premise
if total_purses_premise >= total_purses_hypothesis:
    # check if the estimate of 'total_purses_premise' contradicts the number of total purses in the hypothesis
    label = "contradiction"
elif gift_purses_hypothesis != gift_purses_premise:
    # check if the number of gift purses in the hypothesis contradicts the number of gift purses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

