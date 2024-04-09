premise = "Britain's Whitbread to sell Costa Coffee to Coke for $5.1 billion."
hypothesis = "Coca-Cola expands into coffee with $5.1 billion deal for Britain's Costa."

# compare the number of words in the premise and hypothesis
word_count_premise = len(premise.split())
word_count_hypothesis = len(hypothesis.split())

# check if the number of words in the hypothesis contradicts the number of words in the premise
if word_count_hypothesis!= word_count_premise:
    label = "contradiction"
else:
    # check if the words in the hypothesis contradict the words in the premise
    for word in hypothesis.split():
        if word not in premise.split():
            label = "contradiction"
    # if no contradiction found, infer entailment
    else:
        label = "entailment"

print(label)
