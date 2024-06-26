# define variables for the numerical entities in the premise and hypothesis
premise_score = 100
hypothesis_score = 100

# extract all quantities as valid numbers
premise_score = int(premise_score)
hypothesis_score = int(hypothesis_score)

# compare the scores to infer entailment, contradiction, or neutral
if premise_score > hypothesis_score:
    label = "entailment"
elif premise_score < hypothesis_score:
    label = "contradiction"
else:
    label = "neutral"

print(label)
