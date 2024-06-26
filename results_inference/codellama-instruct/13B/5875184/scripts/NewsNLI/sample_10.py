premise = "A billion is a thousand million, and a trillion is a thousand billion."
hypothesis = "One billion is equal to 1,000 million ; One trillion is equal to 1,000 billion."

# extract the numerical entities from the premise and hypothesis
premise_billion = premise.split(" ")[0]
premise_trillion = premise.split(" ")[2]
hypothesis_billion = hypothesis.split(" ")[0]
hypothesis_trillion = hypothesis.split(" ")[2]

# convert the numerical entities to integers
premise_billion = int(premise_billion)
premise_trillion = int(premise_trillion)
hypothesis_billion = int(hypothesis_billion)
hypothesis_trillion = int(hypothesis_trillion)

# check if the hypothesis values contradict the premise values
if hypothesis_billion!= premise_billion:
    label = "contradiction"
elif hypothesis_trillion!= premise_trillion:
    label = "contradiction"
else:
    label = "entailment"

print(label)
