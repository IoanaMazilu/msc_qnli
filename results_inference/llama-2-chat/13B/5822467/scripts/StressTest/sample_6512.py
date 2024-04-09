x_premise = 7
y_premise = 3
z_premise = 3

x_hypothesis = 7
y_hypothesis = 3
z_hypothesis = 3

# check if the hypothesis values and estimates do not contradict the premise ones
if x_hypothesis == x_premise and y_hypothesis == y_premise and z_hypothesis == z_premise:
    # the hypothesis values and estimates are consistent with the premise ones
    label = "entailment"
elif x_hypothesis!= x_premise or y_hypothesis!= y_premise or z_hypothesis!= z_premise:
    # at least one aspect in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise only gives an estimate for the product of X, Y and Z
    # any product of X, Y and Z consistent with the premise cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
