boys_age_14_premise = 80
boys_age_15_premise = 70
boys_age_13_premise = 50
boys_age_12_premise = 60

boys_age_14_hypothesis = 50
boys_age_15_hypothesis = 70
boys_age_13_hypothesis = 50
boys_age_12_hypothesis = 60

# the hypothesis refers to the number of boys of certain ages in John's School
# the premise gives the actual number of boys of certain ages in John's School

if boys_age_14_premise!= boys_age_14_hypothesis:
    # check if the number of boys of age 14 in the premise contradicts the number of boys of age 14 in the hypothesis
    label = "contradiction"
elif boys_age_15_premise!= boys_age_15_hypothesis:
    # check if the number of boys of age 15 in the premise contradicts the number of boys of age 15 in the hypothesis
    label = "contradiction"
elif boys_age_13_premise!= boys_age_13_hypothesis:
    # check if the number of boys of age 13 in the premise contradicts the number of boys of age 13 in the hypothesis
    label = "contradiction"
elif boys_age_12_premise!= boys_age_12_hypothesis:
    # check if the number of boys of age 12 in the premise contradicts the number of boys of age 12 in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and premise values are the same, we can infer entailment
    label = "entailment"

print(label)
