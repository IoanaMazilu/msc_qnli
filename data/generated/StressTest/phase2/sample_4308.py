# Premise: Of a certain group of 100 people, 40 graduated from High School K, 65 graduated from College Y, and 30 live in City Z.
# Hypothesis: Of a certain group of less than 800 people, 40 graduated from High School K, 65 graduated from College Y, and 30 live in City Z.
# Golden Label: entailment

people_group_premise = 100
people_group_hypothesis = 800
graduated_highschoolK_premise = 40
graduated_highschoolK_hypothesis = 40
graduated_collegeY_premise = 65
graduated_collegeY_hypothesis = 65
live_cityZ_premise = 30
live_cityZ_hypothesis = 30

# The hypothesis refers to the number of people in a group and their attributes mentioned in the premise
if people_group_hypothesis < people_group_premise:
    # Check if the estimate of 'people_group_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
elif (graduated_highschoolK_hypothesis != graduated_highschoolK_premise or 
      graduated_collegeY_hypothesis != graduated_collegeY_premise or 
      live_cityZ_hypothesis != live_cityZ_premise):
    # Check if the number of people with certain attributes in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif people_group_premise < people_group_hypothesis:
    # if the number of people in the premise is less than the number estimated in the hypothesis, we can infer neutrality 
    label = "neutral"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

