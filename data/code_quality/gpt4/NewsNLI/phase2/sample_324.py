people_killed_premise = 21
people_injured_premise = 35
people_killed_hypothesis = 21
people_injured_hypothesis = 35

# the hypothesis mentions the number of people killed and injured, which are also mentioned in the premise
# however, it does not specify the location or event, which are mentioned in the premise
# therefore, we can check if the numbers from the hypothesis contradict the numbers from the premise
if people_killed_hypothesis < people_killed_premise or people_injured_hypothesis < people_injured_premise:
    # check if the number of people killed or injured in the hypothesis is less than the number reported in the premise
    label = "contradiction"
else:
    # if the numbers from the hypothesis do not contradict the numbers from the premise, we infer a neutral relation since the location and event are not specified in the hypothesis
    label = "neutral"

print(label)
