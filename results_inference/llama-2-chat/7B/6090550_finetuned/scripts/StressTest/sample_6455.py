average_score_premise = 66
average_score_hypothesis = 66

# the hypothesis refers to the average score of Andrea in each subject, which is also mentioned in the premise
if average_score_hypothesis < average_score_premise:
    # check if the hypothesis value contradicts the average score in English, Mathematics, Chemistry, Biology, French Language and Physics in the premise
    label = "contradiction"
else:
    # if the hypothesis value is equal to or greater than the average score in the premise, it is entailed
    label = "entailment"

print(label)
