# Premise: If the boys at Jones Elementary make up 30% of the total school population of x students, what is x?
# Hypothesis: If the boys at Jones Elementary make up more than 10% of the total school population of x students, what is x?
# Golden Label: entailment

perc_boys_premise = 30
perc_boys_hypothesis = 10

# the hypothesis refers to the percentage of boys at Jones Elementary mentioned in the premise
if perc_boys_premise < perc_boys_hypothesis:
    # check if the percentage of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
elif perc_boys_premise == perc_boys_hypothesis:
    # check if the percentage of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

