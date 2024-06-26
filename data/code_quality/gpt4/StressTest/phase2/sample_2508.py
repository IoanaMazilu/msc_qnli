group_size_premise = 100
group_size_hypothesis = 600
graduated_hs_premise = 40
graduated_hs_hypothesis = 40
graduated_college_premise = 65
graduated_college_hypothesis = 65
lives_in_city_premise = 30
lives_in_city_hypothesis = 30

# the hypothesis refers to the size of the group and the numbers of high school graduates, college graduates, and city inhabitants mentioned in the premise
if group_size_premise > group_size_hypothesis:
    # check if the estimate of 'group_size_hypothesis' contradicts the size of the group in the premise
    label = "contradiction"
elif graduated_hs_premise != graduated_hs_hypothesis or graduated_college_premise != graduated_college_hypothesis or lives_in_city_premise != lives_in_city_hypothesis:
    # check if the numbers of high school graduates, college graduates, or city inhabitants in the hypothesis contradict the respective numbers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
