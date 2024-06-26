x_premise = 7
y_premise = 3
z_premise = 4

hypothesis_x = 5
hypothesis_y = 5
hypothesis_z = 4

# define variables with representative names for the numerical entities in both inputs
x_premise = x_premise
y_premise = y_premise
z_premise = z_premise

# extract all quantities as valid numbers (integers or floats)
x_hypothesis = int(hypothesis_x)
y_hypothesis = int(hypothesis_y)
z_hypothesis = int(hypothesis_z)

# compare the defined variables
if x_premise <= x_hypothesis:
    # check if the estimate of 'x_hypothesis' contradicts the number of X in the premise
    label = "contradiction"
elif y_premise!= y_hypothesis:
    # check if the number of Y in the hypothesis contradicts the number of Y reported in the premise
    label = "contradiction"
elif z_premise!= z_hypothesis:
    # check if the number of Z in the hypothesis contradicts the number of Z reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
