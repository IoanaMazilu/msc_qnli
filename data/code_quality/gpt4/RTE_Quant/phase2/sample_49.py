sentence_years_premise = 15
sentence_years_hypothesis = 15

# the hypothesis talks about the prison sentence of David A. Feldman, which is also mentioned in the premise
if sentence_years_hypothesis != sentence_years_premise:
    # check if the sentence years in the hypothesis contradicts the sentence years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
