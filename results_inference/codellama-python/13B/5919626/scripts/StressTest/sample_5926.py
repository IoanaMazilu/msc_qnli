purses_faiza_premise = 34
purses_faiza_hypothesis = 14
gifts_faiza_premise = 3
gifts_faiza_hypothesis = 3

# the hypothesis talks about the number of purses and gifts given by Faiza
if purses_faiza_hypothesis <= purses_faiza_premise:
    # check if the hypothesis value contradicts the estimate of less than 'purses_faiza_premise'
    label = "contradiction"
elif gifts_faiza_hypothesis!= gifts_faiza_premise:
    # check if the number of gifts given by Faiza in the hypothesis contradicts the number of gifts given by Faiza in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
