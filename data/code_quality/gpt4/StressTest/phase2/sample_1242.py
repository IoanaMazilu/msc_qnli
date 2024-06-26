group_size_premise = 100
group_size_hypothesis = 600
graduated_hs_premise = 40
graduated_hs_hypothesis = 40
graduated_college_premise = 65
graduated_college_hypothesis = 65
live_city_premise = 30
live_city_hypothesis = 30

# the hypothesis refers to the number of graduates and residents mentioned in the premise
if group_size_hypothesis < group_size_premise:
    # check if the estimate of 'group_size_hypothesis' contradicts the number of people in the group in the premise
    label = "contradiction"
elif graduated_hs_hypothesis != graduated_hs_premise or graduated_college_hypothesis != graduated_college_premise or live_city_hypothesis != live_city_premise:
    # check if the number of graduates or residents in the hypothesis contradicts the number of graduates or residents reported in the premise
    label = "contradiction"
elif group_size_hypothesis > group_size_premise:
    # the premise gives a specific value for the group size
    # any group size less than 'group_size_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones and the group size is the same, we can infer entailment
    label = "entailment"

print(label)
