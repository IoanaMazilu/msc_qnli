words_typed_premise = 8
words_typed_hypothesis = 8
rate_typing_premise = 4
rate_typing_hypothesis = 4

# the hypothesis refers to the number of words typed and the typing rate mentioned in the premise
if words_typed_hypothesis >= words_typed_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif rate_typing_hypothesis!= rate_typing_premise:
    # check if the typing rate in the hypothesis contradicts the typing rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
