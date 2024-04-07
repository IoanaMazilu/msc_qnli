# Premise: Of a certain group of 100 people, 40 graduated from High School O, 65 graduated from College Y, and 30 live in City Z.
# Hypothesis: Of a certain group of 500 people, 40 graduated from High School O, 65 graduated from College Y, and 30 live in City Z.
# Golden Label: contradiction

total_people_premise = 100
total_people_hypothesis = 500
high_school_graduates_premise = 40
high_school_graduates_hypothesis = 40
college_graduates_premise = 65
college_graduates_hypothesis = 65
city_z_residents_premise = 30
city_z_residents_hypothesis = 30

# the hypothesis refers to the same group of people, graduates and residents as the premise
if total_people_hypothesis != total_people_premise:
    # check if the total number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif high_school_graduates_hypothesis != high_school_graduates_premise:
    # check if the number of high school graduates in the hypothesis contradicts the number of high school graduates in the premise
    label = "contradiction"
elif college_graduates_hypothesis != college_graduates_premise:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates in the premise
    label = "contradiction"
elif city_z_residents_hypothesis != city_z_residents_premise:
    # check if the number of City Z residents in the hypothesis contradicts the number of City Z residents in the premise
    label = "contradiction"
else:
    # if the hypothesis values and counts do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

