# the hypothesis talks about the number of tests taken by Joe and the average score obtained
test_scores_premise = 60
test_scores_hypothesis = 60

# the hypothesis refers to the number of tests taken by Joe and the average score obtained
if test_scores_premise <= test_scores_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than 'test_scores_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of tests taken by Joe
    # any number of tests greater than 'test_scores_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
