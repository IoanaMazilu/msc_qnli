# Premise: Of a certain group of 100 people, 40 graduated from High School M, 65 graduated from College Y, and 30 live in City Z.
# Hypothesis: Of a certain group of 500 people, 40 graduated from High School M, 65 graduated from College Y, and 30 live in City Z.
# Golden Label: contradiction

group_size_premise = 100
group_size_hypothesis = 500
hs_graduates_premise = 40
hs_graduates_hypothesis = 40
college_graduates_premise = 65
college_graduates_hypothesis = 65
city_residents_premise = 30
city_residents_hypothesis = 30

# the hypothesis refers to the same group of people described in the premise
# it provides the same numbers for high school graduates, college graduates and city residents
# but it increases the size of the group to 500, contradicting the premise
if hs_graduates_premise != hs_graduates_hypothesis:
    # check if the number of high school graduates in the hypothesis contradicts the premise
    label = "contradiction"
elif college_graduates_premise != college_graduates_hypothesis:
    # check if the number of college graduates in the hypothesis contradicts the premise
    label = "contradiction"
elif city_residents_premise != city_residents_hypothesis:
    # check if the number of city residents in the hypothesis contradicts the premise
    label = "contradiction"
elif group_size_premise != group_size_hypothesis:
    # check if the size of the group in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

