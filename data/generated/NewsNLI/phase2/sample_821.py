# Premise: Charges against Alton Alexander Nolen, 30, will include first-degree murder and assault with a deadly weapon, according to Jeremy Lewis, spokesman for the Moore, Oklahoma, police.
# Hypothesis: Police say they have interviewed suspect Alton Alexander Nolen, 30.
# Golden Label: neutral

age_premise = 30
age_hypothesis = 30

# The hypothesis mentions the age of the suspect Alton Alexander Nolen, which is also mentioned in the premise
if age_hypothesis != age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis age does not contradict the premise age, we can infer entailment as hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either.
    label = "neutral"

print(label)

