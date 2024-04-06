# Premise: -- Sandy killed at least six people in the state, said Gov.
# Hypothesis: Sandy has killed at least 56 people in the United States.
# Golden Label: neutral

people_killed_premise = 6
people_killed_hypothesis = 56

# the hypothesis mentions the total number of people killed in the US, which is higher than the number reported in the premise
if people_killed_hypothesis <= people_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise we can infer neutrality
    label = "neutral"

print(label)

