sentence_premise = "this sentence is ultimately legal"
sentence_hypothesis = "it is an immoral one"

# the hypothesis mentions the sentence being legal, which is also mentioned in the premise
if sentence_hypothesis!= sentence_premise:
    # check if the sentence in the hypothesis contradicts the sentence in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
