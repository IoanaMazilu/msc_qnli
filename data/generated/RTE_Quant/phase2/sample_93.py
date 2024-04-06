# Premise: Insurgents exposed the vulnerability of Iraq's security forces again Sunday, killing at least 22 national guardsmen and their driver in a suicide bombing and 10 other people in separate attacks with elections just weeks away.
# Hypothesis: A suicide bomber blew up his vehicle killing at least 14 people.
# Golden Label: neutral

guardsmen_killed_premise = 22
driver_killed_premise = 1
other_people_killed_premise = 10
total_people_killed_premise = guardsmen_killed_premise + driver_killed_premise + other_people_killed_premise
people_killed_hypothesis = 14

# the hypothesis talks about the number of people killed by a suicide bomber, which is also mentioned in the premise
if people_killed_hypothesis > total_people_killed_premise:
    # check if the number of people killed in the hypothesis contradicts the total number of people killed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

