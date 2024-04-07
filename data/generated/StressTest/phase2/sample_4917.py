# Premise: Of a certain group of 100 people, 40 graduated from High School A, 65 graduated from College Y, and 30 live in City Z.
# Hypothesis: Of a certain group of less than 300 people, 40 graduated from High School A, 65 graduated from College Y, and 30 live in City Z.
# Golden Label: entailment

group_size_premise = 100
group_size_hypothesis = 300
high_school_graduates_premise = 40
high_school_graduates_hypothesis = 40
college_graduates_premise = 65
college_graduates_hypothesis = 65
city_residents_premise = 30
city_residents_hypothesis = 30

# the hypothesis refers to the same group of people mentioned in the premise
if high_school_graduates_hypothesis != high_school_graduates_premise or college_graduates_hypothesis != college_graduates_premise or city_residents_hypothesis != city_residents_premise:
    # check if the number of high school graduates, college graduates, or city residents contradicts the numbers reported in the premise
    label = "contradiction"
elif group_size_hypothesis < group_size_premise:
    # check if the size of the group in the hypothesis contradicts the size of the group in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

