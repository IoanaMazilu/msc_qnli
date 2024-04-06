# Premise: They remember Dylan Hockley, 6, as always smiling and full of joy.
# Hypothesis: He was 6 and full of joy, his mother, Nicole Hockley, says.
# Golden Label: entailment

age_premise = 6
age_hypothesis = 6

# the hypothesis mentions the age of the boy, which is also referenced in the premise
if age_hypothesis != age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the age values do not contradict, we can infer entailment
    label = "entailment"

print(label)

