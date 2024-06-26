words_premise = 25
words_hypothesis = 65
rate = 5

# the hypothesis refers to the number of words typed and the rate of typing mentioned in the premise
time_premise = words_premise / rate
time_hypothesis = words_hypothesis / rate

if time_premise != time_hypothesis:
    # check if the estimated time in the hypothesis contradicts the estimated time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment or neutral
    # but in this case, since the numbers of words are different, we can safely infer contradiction
    label = "contradiction"

print(label)
