# Premise: The provincial governor, Abdul Haq Shafaq, said six Afghans were killed and 20 others were wounded.
# Hypothesis: Three American troops were wounded, the governor said.
# Golden Label: neutral

afghans_killed_premise = 6
afghans_wounded_premise = 20
american_troops_wounded_hypothesis = 3

# the hypothesis mentions a number of American troops wounded, which is not referenced in the premise
# therefore, we cannot entail or contradict this information from the premise
# the premise also mentions the number of Afghans killed and wounded, which is not referenced in the hypothesis
# so we also cannot entail or contradict this information from the hypothesis
label = "neutral"

print(label)

