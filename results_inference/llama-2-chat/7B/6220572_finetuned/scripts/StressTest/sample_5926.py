purses_premise = 34
purses_hypothesis = 14
gifts_premise = 3
gifts_hypothesis = 3

# the hypothesis talks about the number of purses and gifts, referenced also in the premise
if purses_hypothesis >= purses_premise:
    # check if the estimate of 'purses_hypothesis' contradicts the number of purses in the premise
    label = "contradiction"
elif gifts_hypothesis!= gifts_premise:
    # check if the number of gifts in the hypothesis contradicts the number of gifts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
