# defining the variables from the premise and hypothesis
group_size_premise = 100
group_size_hypothesis = 600
hs_graduates_premise = 40
hs_graduates_hypothesis = 40
college_graduates_premise = 65
college_graduates_hypothesis = 65
city_residents_premise = 30
city_residents_hypothesis = 30

# compare sizes of the groups in premise and hypothesis
if group_size_premise != group_size_hypothesis:
    label = "contradiction"
# compare the number of High School K graduates in premise and hypothesis
elif hs_graduates_hypothesis != hs_graduates_premise:
    label = "contradiction"
# compare the number of College Y graduates in premise and hypothesis
elif college_graduates_hypothesis != college_graduates_premise:
    label = "contradiction"
# compare the number of City Z residents in premise and hypothesis
elif city_residents_hypothesis != city_residents_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
