people_group_premise = 100
people_group_hypothesis = 800
graduated_highSchoolL_premise = 40
graduated_highSchoolL_hypothesis = 40
graduated_collegeY_premise = 65
graduated_collegeY_hypothesis = 65
living_cityZ_premise = 30
living_cityZ_hypothesis = 30

# the hypothesis refers to the number of people, the number of people graduated from High School L and College Y, and the number of people living in City Z mentioned in the premise
if people_group_hypothesis < people_group_premise:
    # check if the estimate of 'people_group_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
elif graduated_highSchoolL_hypothesis != graduated_highSchoolL_premise or graduated_collegeY_hypothesis != graduated_collegeY_premise or living_cityZ_hypothesis != living_cityZ_premise:
    # check if the number of people graduated from High School L, College Y, and living in City Z in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
elif people_group_hypothesis == people_group_premise:
    # if the hypothesis values and estimates do not contradict the premise ones and the number of people matches, we can infer entailment
    label = "entailment"
else:
    # the premise gives the exact number of people
    # any number of people greater than 'people_group_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
