people_group_premise = 600
people_group_hypothesis = 100
high_school_graduates_premise = 40
high_school_graduates_hypothesis = 40
college_graduates_premise = 65
college_graduates_hypothesis = 65
city_residents_premise = 30
city_residents_hypothesis = 30

# the hypothesis refers to the same group of people, high school graduates, college graduates and city residents as the premise
if people_group_hypothesis >= people_group_premise:
    # check if the number of people in the group according to the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif high_school_graduates_hypothesis != high_school_graduates_premise or college_graduates_hypothesis != college_graduates_premise or city_residents_hypothesis != city_residents_premise:
    # check if the number of high school graduates, college graduates or city residents in the hypothesis contradicts the corresponding number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
