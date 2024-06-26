total_people_premise = 600
total_people_hypothesis = 100
high_school_graduates_premise = 40
high_school_graduates_hypothesis = 40
college_graduates_premise = 65
college_graduates_hypothesis = 65
city_z_residents_premise = 30
city_z_residents_hypothesis = 30

# the hypothesis refers to the number of people, high school graduates, college graduates, and residents of City Z mentioned in the premise
if total_people_hypothesis >= total_people_premise:
    # check if the total number of people in the hypothesis contradicts the estimate of less than 'total_people_premise'
    label = "contradiction"
elif high_school_graduates_hypothesis != high_school_graduates_premise:
    # check if the number of high school graduates in the hypothesis contradicts the number of high school graduates reported in the premise
    label = "contradiction"
elif college_graduates_hypothesis != college_graduates_premise:
    # check if the number of college graduates in the hypothesis contradicts the number of college graduates reported in the premise
    label = "contradiction"
elif city_z_residents_hypothesis != city_z_residents_premise:
    # check if the number of residents of City Z in the hypothesis contradicts the number of residents of City Z reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
