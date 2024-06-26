purses_faiza_premise = 8
purses_faiza_hypothesis = 8
gifts_faiza_premise = 3
gifts_faiza_hypothesis = 3

# the premise and hypothesis are consistent with each other
if purses_faiza_premise!= purses_faiza_hypothesis:
    # check if the number of purses in the premise contradicts the number of purses in the hypothesis
    label = "contradiction"
elif gifts_faiza_premise!= gifts_faiza_hypothesis:
    # check if the number of gifts in the premise contradicts the number of gifts in the hypothesis
    label = "contradiction"
else:
    # the premise and hypothesis are consistent with each other
    label = "entailment"

print(label)
