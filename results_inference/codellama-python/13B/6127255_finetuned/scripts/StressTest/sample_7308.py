words_premise = 8
words_hypothesis = 7
typing_rate = 4

# the hypothesis refers to the number of words James types and the typing rate mentioned in the premise
if words_hypothesis >= words_premise:
    # check if the estimate of 'words_hypothesis' contradicts the number of words in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
