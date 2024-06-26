total_people_premise = 100
total_people_hypothesis = 600
high_school_graduates_premise = 40
high_school_graduates_hypothesis = 40
college_graduates_premise = 65
college_graduates_hypothesis = 65
city_z_residents_premise = 30
city_z_residents_hypothesis = 30

# the hypothesis refers to the same group of people, graduates and residents as in the premise
if total_people_hypothesis != total_people_premise:
    # check if the total number of people in the hypothesis contradicts the total number of people in the premise
    label = "contradiction"
elif high_school_graduates_hypothesis != high_school_graduates_premise:
    # check if the number of graduates from High School A in the hypothesis contradicts the number of such graduates in the premise
    label = "contradiction"
elif college_graduates_hypothesis != college_graduates_premise:
    # check if the number of graduates from College Y in the hypothesis contradicts the number of such graduates in the premise
    label = "contradiction"
elif city_z_residents_hypothesis != city_z_residents_premise:
    # check if the number of residents in City Z in the hypothesis contradicts the number of such residents in the premise
    label = "contradiction"
else:
    # if the hypothesis numbers do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
