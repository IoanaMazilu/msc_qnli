words_typed_premise = 8
words_typed_hypothesis = 7
typing_rate_premise = 4
typing_rate_hypothesis = 4

# the hypothesis refers to the number of words typed by James, which is also mentioned in the premise
# compute the number of words James can type in the given time
can_type_words_premise = (words_typed_premise / typing_rate_premise) * 60
if can_type_words_premise <= words_typed_hypothesis:
    # check if the estimate of 'words_typed_hypothesis' contradicts the number of words James can type in the premise
    label = "contradiction"
elif can_type_words_premise > words_typed_hypothesis:
    # check if the number of words James can type in the hypothesis contradicts the number of words he can type in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
