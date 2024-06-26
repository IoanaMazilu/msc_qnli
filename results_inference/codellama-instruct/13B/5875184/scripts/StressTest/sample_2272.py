premise = "What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is less than 4:3?"
hypothesis = "What is the average speed of Murali from A to C given that the ratio of distances between A to B and B to C is 2:3?"

# extract the numerical entities from the premise and hypothesis
premise_ratio = float(premise.split("is less than")[1].split(":")[0])
hypothesis_ratio = float(hypothesis.split("is")[1].split(":")[0])

# check if the hypothesis ratio contradicts the premise ratio
if hypothesis_ratio > premise_ratio:
    label = "contradiction"
# check if the hypothesis ratio is consistent with the premise ratio
elif hypothesis_ratio <= premise_ratio:
    label = "neutral"
# check if the hypothesis ratio entails the premise ratio
else:
    label = "entailment"

print(label)
