# Premise: All 11 remains were of African-American women.
# Hypothesis: Anthony Sowell accused in deaths of 11 women.
# Golden Label: neutral

remains_premise = 11
deaths_hypothesis = 11

# the hypothesis mentions the number of women's deaths, which is also mentioned in the premise
# however, the hypothesis introduces a new entity (Anthony Sowell) that is not mentioned in the premise
# there is also no mention in the hypothesis about the ethnicity of the women, which is stated in the premise
if remains_premise != deaths_hypothesis:
    # check if the number of deaths in the hypothesis contradicts the number of remains reported in the premise
    label = "contradiction"
else:
    # if the number mentioned in the hypothesis does not contradict the number in the premise, we can infer neutrality
    label = "neutral"

print(label)

