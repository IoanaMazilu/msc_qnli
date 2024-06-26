# defining the premise and hypothesis scores
premise_scores = [7, 2, 3, 4]
hypothesis_scores = [1, 2, 3, 4]

# checking if the premise and hypothesis scores are the same
if premise_scores!= hypothesis_scores:
    # if the scores are not the same, we have a contradiction
    label = "contradiction"
else:
    # if the scores are the same, we have a neutral situation
    label = "neutral"

print(label)
