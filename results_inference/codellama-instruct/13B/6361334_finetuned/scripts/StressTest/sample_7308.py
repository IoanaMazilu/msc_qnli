words_per_minute_premise = 4
words_per_minute_hypothesis = 4
words_to_type_premise = 8
words_to_type_hypothesis = 7

# the hypothesis refers to the number of words to type mentioned in the premise
if words_to_type_hypothesis <= words_to_type_premise:
    # check if the estimate of 'words_to_type_hypothesis' contradicts the number of words to type in the premise
    label = "contradiction"
elif words_per_minute_hypothesis!= words_per_minute_premise:
    # check if the rate of typing in the hypothesis contradicts the rate of typing reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
