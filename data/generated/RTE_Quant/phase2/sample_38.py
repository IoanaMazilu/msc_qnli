# Premise: A federal judge sentenced an apparently stunned Michael Milken to 10 years in prison Wednesday after ruling that the crimes he pleaded guilty to were neither minor nor isolated.
# Hypothesis: Milken was given a 10-year sentence.
# Golden Label: entailment

sentence_length_premise = 10
sentence_length_hypothesis = 10

# the hypothesis mentions the length of the sentence given to Milken, which is also mentioned in the premise
if sentence_length_hypothesis != sentence_length_premise:
    # check if the length of the sentence in the hypothesis contradicts the length of the sentence from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

