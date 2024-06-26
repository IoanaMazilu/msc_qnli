economics_class_premise = 16
marketing_class_premise = 28
statistics_class_premise = 18

economics_class_hypothesis = 56
marketing_class_hypothesis = 28
statistics_class_hypothesis = 18

# the hypothesis refers to the number of names in the rosters for each of Professor Wang's classes mentioned in the premise
if economics_class_hypothesis != economics_class_premise:
    # check if the number of names in the roster for the economics class in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif marketing_class_hypothesis != marketing_class_premise:
    # check if the number of names in the roster for the marketing class in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif statistics_class_hypothesis != statistics_class_premise:
    # check if the number of names in the roster for the statistics class in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the numbers in the hypothesis do not contradict the numbers reported in the premise, we can infer entailment
    label = "entailment"

print(label)
