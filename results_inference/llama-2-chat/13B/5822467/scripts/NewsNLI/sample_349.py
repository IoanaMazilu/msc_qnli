heller_premise = "I can sum it up in one word:ridiculous,"
heller_hypothesis = "I can sum it up in one word:ridiculous,"

# extract numerical information from the input sentences
heller_premise_num = len(heller_premise.split())
heller_hypothesis_num = len(heller_hypothesis.split())

# compare the numerical information
if heller_premise_num == heller_hypothesis_num:
    # if the number of words in the premise and hypothesis are the same, we can infer neutrality
    label = "neutral"
elif heller_premise_num < heller_hypothesis_num:
    # if the number of words in the hypothesis is greater than the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of words in the premise is greater than the hypothesis, we can infer contradiction
    label = "contradiction"

print(label)
