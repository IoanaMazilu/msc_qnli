# Premise: According to the United Nations, more than 100,000 people have been killed since fighting began.
# Hypothesis: About 100,000 killed, 6 million displaced since fighting began, U.N. says.
# Golden Label: neutral

people_killed_premise = 100000
people_killed_hypothesis = 100000
people_displaced_hypothesis = 6000000

# the hypothesis mentions the number of killed people, which is also mentioned in the premise
# however, the hypothesis also mentions the number of displaced people, which cannot be entailed from the premise
if people_killed_hypothesis != people_killed_premise:
    # check if the number of killed people in the hypothesis contradicts the number of killed people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality because the hypothesis has additional information not present in the premise
    label = "neutral"

print(label)

