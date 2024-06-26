words_typed_premise = 8
words_typed_hypothesis = 8
typing_rate_premise = 4
typing_rate_hypothesis = 4

# the hypothesis refers to the number of words James types, which is also mentioned in the premise
# compute the maximum number of words James can type if he types at the same rate as in the premise
maximum_words_hypothesis = words_typed_premise / typing_rate_hypothesis

if maximum_words_hypothesis >= words_typed_premise:
    # check if the estimate of'maximum_words_hypothesis' contradicts the number of words typed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
