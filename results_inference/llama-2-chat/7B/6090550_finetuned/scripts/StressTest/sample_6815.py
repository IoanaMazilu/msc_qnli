y_premise = 18%
y_hypothesis = 58%

# the hypothesis refers to the percentage of students with cars, mentioned in the premise
if y_premise!= y_hypothesis:
    # check if the percentage of students with cars in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentages match, we can infer entailment
    label = "entailment"

print(label)
