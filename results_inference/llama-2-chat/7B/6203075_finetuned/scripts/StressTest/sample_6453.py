average_score_premise = (66 + 60 + 72 + 77 + 55 + 85) / 6
average_score_hypothesis = (less_than_76 + 60 + 72 + 77 + 55 + 85) / 6

# the hypothesis refers to the average scores of Andrea in different subjects
if average_score_hypothesis == average_score_premise:
    # check if the average score in the hypothesis is the same as in the premise
    label = "entailment"
elif average_score_hypothesis!= average_score_premise:
    # check if the average score in the hypothesis contradicts the average score in the premise
    label = "contradiction"
else:
    # if the average scores in the hypothesis and premise are the same, we can infer neutrality
    label = "neutral"

print(label)
