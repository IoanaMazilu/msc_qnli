words_premise = 8
words_hypothesis = 8
typing_rate_premise = 4
typing_rate_hypothesis = 4

# the hypothesis refers to the number of words James types and his typing rate, mentioned in the premise
if words_hypothesis >= words_premise:
    # check if the number of words in the hypothesis contradicts the number of words in the premise
    label = "contradiction"
elif typing_rate_hypothesis!= typing_rate_premise:
    # check if the typing rate in the hypothesis contradicts the typing rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
