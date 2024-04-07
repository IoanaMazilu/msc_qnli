# Premise: Of a certain group of less than 300 people, 40 graduated from High School A, 65 graduated from College Y, and 30 live in City Z.
# Hypothesis: Of a certain group of 100 people, 40 graduated from High School A, 65 graduated from College Y, and 30 live in City Z.
# Golden Label: neutral

group_people_premise = 300
group_people_hypothesis = 100
graduated_A_premise = 40
graduated_A_hypothesis = 40
graduated_Y_premise = 65
graduated_Y_hypothesis = 65
live_Z_premise = 30
live_Z_hypothesis = 30

# the hypothesis refers to the same group of people, their graduation and city of residence as mentioned in the premise
if group_people_hypothesis >= group_people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif graduated_A_hypothesis != graduated_A_premise:
    # check if the number of people who graduated from A in the hypothesis contradicts the number of people who graduated from A in the premise
    label = "contradiction"
elif graduated_Y_hypothesis != graduated_Y_premise:
    # check if the number of people who graduated from Y in the hypothesis contradicts the number of people who graduated from Y in the premise
    label = "contradiction"
elif live_Z_hypothesis != live_Z_premise:
    # check if the number of people who live in Z in the hypothesis contradicts the number of people who live in Z in the premise
    label = "contradiction"
else:
    # the number of people in the hypothesis is less than in the premise, and the other figures are the same
    # so the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

