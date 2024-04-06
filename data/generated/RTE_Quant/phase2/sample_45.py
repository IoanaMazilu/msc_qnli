# Premise: Leona Helmsley, the self-proclaimed queen of a luxury hotel chain, was sentenced Tuesday to four years in federal prison.
# Hypothesis: Leona Helmsley was given a four year sentence.
# Golden Label: entailment

sentence_years_premise = 4
sentence_years_hypothesis = 4

# the hypothesis talks about the same person and the same sentence years as in the premise
if sentence_years_hypothesis != sentence_years_premise:
    # check if the sentence years in the hypothesis contradicts the sentence years in the premise
    label = "contradiction"
else:
    # if the sentence years in the hypothesis does not contradict the sentence years in the premise, we can infer entailment
    label = "entailment"

print(label)

