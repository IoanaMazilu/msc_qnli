# Premise: At least 100 Americans have either left or attempted to leave to go to Syria and help ISIS, Johnson said.
# Hypothesis: He says at least 100 Americans have tried to go fight with ISIS in Syria.
# Golden Label: entailment

americans_premise = 100
americans_hypothesis = 100

# the hypothesis mentions the number of Americans who tried to go fight with ISIS in Syria, which is also referenced in the premise

# check if the number of Americans in the hypothesis contradicts the number of Americans in the premise
if americans_hypothesis != americans_premise:
    label = "contradiction"
else:
    # if the number of Americans in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

