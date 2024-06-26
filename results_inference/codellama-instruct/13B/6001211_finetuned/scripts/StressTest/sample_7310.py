words_premise = 8
words_hypothesis = 8
typing_rate = 4

# the hypothesis refers to the number of words James types, mentioned in the premise
if words_hypothesis >= words_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
