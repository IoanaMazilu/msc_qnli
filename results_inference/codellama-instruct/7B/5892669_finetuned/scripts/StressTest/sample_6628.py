# defining the premise and hypothesis scores
premise_scores = [8, 2, 3]
hypothesis_scores = [1, 2, 3]

# checking if the hypothesis scores are less than the premise scores
for i in range(len(premise_scores)):
    if hypothesis_scores[i] >= premise_scores[i]:
        # if the hypothesis score is not less than the premise score, it's a contradiction
        label = "contradiction"
        break
else:
    # if the hypothesis scores are all less than the premise scores, it's entailment
    label = "entailment"

print(label)
