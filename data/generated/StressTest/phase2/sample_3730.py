# Premise: Of a certain group of less than 800 people, 40 graduated from High School L, 65 graduated from College Y, and 30 live in City Z.
# Hypothesis: Of a certain group of 100 people, 40 graduated from High School L, 65 graduated from College Y, and 30 live in City Z.
# Golden Label: neutral

people_group_premise = 800
people_group_hypothesis = 100
high_school_grads_premise = 40
high_school_grads_hypothesis = 40
college_grads_premise = 65
college_grads_hypothesis = 65
city_residents_premise = 30
city_residents_hypothesis = 30

# the hypothesis refers to the same groups of people mentioned in the premise
# first, we compare the total number of people in the group
if people_group_hypothesis >= people_group_premise:
    # check if the number of people in the group according to the hypothesis contradicts the 'less than 800' estimate in the premise
    label = "contradiction"
elif high_school_grads_hypothesis != high_school_grads_premise:
    # check if the number of high school graduates in the hypothesis contradicts the number of high school graduates reported in the premise
    label = "contradiction"
elif college_grads_hypothesis != college_grads_premise:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
elif city_residents_hypothesis != city_residents_premise:
    # check if the number of city residents in the hypothesis contradicts the number of city residents reported in the premise
    label = "contradiction"
else:
    # if all the values in the hypothesis do not contradict the ones in the premise, but the total number of people is not explicitly entailed in the premise
    label = "neutral"

print(label)

