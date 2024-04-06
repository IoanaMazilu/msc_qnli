# Premise: The idea that schizophrenia is not one single disorder is not really new, says Dr. Charles Raison, a professor of psychiatry at the University of Arizona.
# Hypothesis: Researchers say schizophrenia is not one disorder, but eight.
# Golden Label: neutral

disorders_premise = 1
disorders_hypothesis = 8

# the hypothesis mentions the number of disorders related to schizophrenia, which is also mentioned in the premise
if disorders_hypothesis > disorders_premise:
    # check if the number of disorders in the hypothesis contradicts the number of disorders mentioned in the premise
    label = "contradiction"
else:
    # if the number of disorders in the hypothesis does not contradict the number of disorders in the premise, we can infer entailment
    label = "entailment"

print(label)

