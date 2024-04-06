# Premise: In the study involving nearly 6,000 African American participants aged 60 or older, about 2,000 of whom had Alzheimer's and 4,000 who did not, variants in the genes ABCA7 and ApoE increased risk of developing Alzheimer's by 80% and more than two fold, respectively.
# Hypothesis: Study involved nearly 6,000 African American participants aged 60 or older.
# Golden Label: entailment

participants_premise = 6000
participants_hypothesis = 6000

# the hypothesis mentions the number of participants in the study, which is also mentioned in the premise
if participants_hypothesis != participants_premise:
    # check if the number of participants in the hypothesis contradicts the number of participants in the premise
    label = "contradiction"
else:
    # if the number in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

