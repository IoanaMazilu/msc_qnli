random_processing_premise = 112
scramjet_premise = 234
both_premise = 112

random_processing_hypothesis = 312
scramjet_hypothesis = 234
both_hypothesis = 112

# the hypothesis talks about the number of students studying each subject, referenced also in the premise
if random_processing_hypothesis <= random_processing_premise and scramjet_hypothesis <= scramjet_premise and both_hypothesis <= both_premise:
    # check if the hypothesis values contradict the estimate of 'random_processing_premise','scramjet_premise', and 'both_premise'
    label = "contradiction"
elif random_processing_hypothesis > random_processing_premise or scramjet_hypothesis > scramjet_premise or both_hypothesis > both_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students studying each subject
    # any number of students studying each subject greater than the premise value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
