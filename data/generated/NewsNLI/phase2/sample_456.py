# Premise: The city's al-Jalaa Hospital said it received the bodies of three soldiers killed in fighting that broke out in the eastern Sidi Khalifa district.
# Hypothesis: Hospital says it received bodies of 3 soldiers killed in fighting in the eastern part of the city.
# Golden Label: entailment

soldiers_premise = 3
soldiers_hypothesis = 3

# the hypothesis mentions the number of soldiers' bodies received by the hospital, which is also mentioned in the premise
if soldiers_hypothesis != soldiers_premise:
    # check if the number of soldiers in the hypothesis contradicts the number of soldiers reported in the premise
    label = "contradiction"
else:
    # if the number of soldiers from the hypothesis does not contradict the number from the premise, we can infer entailment
    label = "entailment"

print(label)

