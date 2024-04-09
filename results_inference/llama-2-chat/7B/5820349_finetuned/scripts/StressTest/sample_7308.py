words_premise = 8
words_hypothesis = 7
rate_premise = 4
rate_hypothesis = 4

# the hypothesis refers to the number of words and typing rate mentioned in the premise
if words_premise <= words_hypothesis:
    # check if the number of words in the hypothesis contradicts the number of words in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the typing rate in the hypothesis contradicts the typing rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
