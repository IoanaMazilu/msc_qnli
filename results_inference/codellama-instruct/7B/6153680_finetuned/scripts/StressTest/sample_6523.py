scores = [45, 67, 76, 82, 85]
new_scores = [55, 67, 76, 82, 85]

# the hypothesis refers to the scores obtained by Reeya in different subjects
# the premise gives the scores obtained by Reeya

# the hypothesis and premise both give the same scores
if new_scores!= scores:
    # check if the scores in the hypothesis and premise are the same
    label = "contradiction"
else:
    # if the scores are the same, we can infer entailment
    label = "entailment"

print(label)
