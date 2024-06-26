men_serving_sentences_premise = 4
men_serving_sentences_hypothesis = 4

# the hypothesis mentions the number of men serving sentences in U.S. prisons, which is also mentioned in the premise
if men_serving_sentences_hypothesis != men_serving_sentences_premise:
    # check if the number of men from the hypothesis contradicts the number of men reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
