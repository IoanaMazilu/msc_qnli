# Premise: Israeli helicopters shot two missiles at a car driving through the Gaza Strip on Wednesday, killing three people, Palestinian security sources said.
# Hypothesis: Three militants from the Islamic Jihad group were killed when Israeli helicopters fired missiles at a car in the Gaza Strip.
# Golden Label: neutral

missiles_premise = 2
missiles_hypothesis = 2
people_killed_premise = 3
people_killed_hypothesis = 3

# the hypothesis talks about the number of missiles and the number of people killed which are also mentioned in the premise
if missiles_hypothesis != missiles_premise:
    # check if the number of missiles in the hypothesis contradicts the number of missiles in the premise
    label = "contradiction"
elif people_killed_hypothesis != people_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
