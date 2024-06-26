# define variables for the numerical entities in the premise and hypothesis
premise_score = 0
hypothesis_score = 0

# extract the numerical entities from the premise and hypothesis
premise_score = int(premise.split(" ")[-1])
hypothesis_score = int(hypothesis.split(" ")[-1])

# compare the scores from the premise and hypothesis
if premise_score > hypothesis_score:
    # check if the score in the premise is higher than the score in the hypothesis
    label = "entailment"
elif premise_score < hypothesis_score:
    # check if the score in the premise is lower than the score in the hypothesis
    label = "contradiction"
else:
    # if the scores are equal, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
