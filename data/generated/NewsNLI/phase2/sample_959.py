# Premise: A spokesman from Peshawar's Lady Reading Hospital says that the three people killed included a woman, a civilian and a member of the Frontier Corps.
# Hypothesis: A suicide blast has killed 3 and injured 13 in Peshawar, Pakistan.
# Golden Label: neutral

killed_premise = 3
killed_hypothesis = 3
injured_hypothesis = 13

# the hypothesis mentions the number of people killed in Peshawar, which is also referenced in the premise
# however, the hypothesis also mentions the number of people injured, which cannot be entailed from the premise
if killed_hypothesis != killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed reported in the premise
    label = "contradiction"
else:
    # if the number of people killed in the hypothesis does not contradict the number of people killed in the premise and 
    # there is no information about the number of people injured in the premise, we can infer neutrality
    label = "neutral"

print(label)

