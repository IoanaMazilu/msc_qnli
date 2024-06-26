average_score_premise = (66 + 60 + 72 + 77 + 55 + 85) / 6
average_score_hypothesis = (less_than_66 + 60 + 72 + 77 + 55 + 85) / 6

# the hypothesis refers to the scores in the examination, which are also mentioned in the premise
if average_score_premise == average_score_hypothesis:
    label = "entailment"
elif average_score_premise!= average_score_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
