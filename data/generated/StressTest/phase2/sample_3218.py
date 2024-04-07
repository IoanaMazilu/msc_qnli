# Premise: If 6 years are subtracted from the present age of Arun and the remainder is divided by 18, then the present age of his grandson Gokul is obtained.
# Hypothesis: If more than 6 years are subtracted from the present age of Arun and the remainder is divided by 18, then the present age of his grandson Gokul is obtained.
# Golden Label: contradiction

years_subtracted_premise = 6
years_subtracted_hypothesis = 6

# the hypothesis refers to the same procedure as the premise, but with a different number of subtracted years
if years_subtracted_hypothesis > years_subtracted_premise:
    # check if the number of subtracted years in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the number of subtracted years in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

