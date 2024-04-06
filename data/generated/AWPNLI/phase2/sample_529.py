# Premise: In a school, there are 542.0 girls and 387.0 boys.
# Hypothesis: 154.0 more girls are there compared to boys in that school.
# Golden Label: contradiction

girls_premise = 542.0
boys_premise = 387.0
more_girls_hypothesis = 154.0

# the hypothesis refers to the difference in the number of girls and boys, which is also mentioned in the premise
# compute the difference in the number of girls and boys in the premise
difference_girls_boys_premise = girls_premise - boys_premise
if more_girls_hypothesis != difference_girls_boys_premise:
    # check if the difference in the number of girls and boys in the hypothesis contradicts the difference from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

