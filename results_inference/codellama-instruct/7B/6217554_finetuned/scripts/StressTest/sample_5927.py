purses_premise = 14
purses_hypothesis = 34
gift_premise = 3
gift_hypothesis = 3

# the hypothesis gives a total number of purses and a gift, referenced also in the premise
if purses_hypothesis <= purses_premise:
    # check if the number of purses in the hypothesis contradicts the number of purses reported in the premise
    label = "contradiction"
elif gift_hypothesis!= gift_premise:
    # check if the number of gifts in the hypothesis contradicts the number of gifts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
