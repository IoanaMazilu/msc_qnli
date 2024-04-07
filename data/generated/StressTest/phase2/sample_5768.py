# Premise: If Dana gives her parents 5% of that amount back each month, how much will she still owe her parents after four years of college?
# Hypothesis: If Dana gives her parents 1% of that amount back each month, how much will she still owe her parents after four years of college?
# Golden Label: contradiction

percentage_given_back_premise = 5
percentage_given_back_hypothesis = 1

# the hypothesis refers to the percentage given back each month by Dana, which is also mentioned in the premise
if percentage_given_back_hypothesis != percentage_given_back_premise:
    # check if the percentage given back each month in the hypothesis contradicts the percentage given back each month reported in the premise
    label = "contradiction"
else:
    # if the percentage given back each month in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
