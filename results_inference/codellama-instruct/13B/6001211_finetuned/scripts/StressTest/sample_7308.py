words_premise = 8
words_hypothesis = 7
typing_rate = 4

# the hypothesis refers to the time it would take James to type a certain number of words at a given rate, as mentioned in the premise
if words_hypothesis >= words_premise:
    # check if the number of words in the hypothesis contradicts the number of words in the premise
    label = "contradiction"
else:
    # if the number of words in the hypothesis is less than the number of words in the premise, we can infer entailment
    label = "entailment"

print(label)
