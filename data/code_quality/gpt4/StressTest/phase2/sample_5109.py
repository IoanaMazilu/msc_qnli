roseline_age_premise = 50
roseline_age_hypothesis = 60
daughter_age_premise = 20
daughter_age_hypothesis = 20

# the hypothesis refers to the ages of Roseline and her daughter mentioned in the premise
if roseline_age_premise >= roseline_age_hypothesis:
    # check if 'roseline_age_premise' contradicts the maximum age of Roseline stated in the hypothesis
    label = "contradiction"
elif daughter_age_hypothesis != daughter_age_premise:
    # check if the age of the daughter in the hypothesis contradicts the age of the daughter reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
