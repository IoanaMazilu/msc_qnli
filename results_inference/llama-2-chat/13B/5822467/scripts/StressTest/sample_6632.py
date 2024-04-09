# define variables with representative names for the numerical entities in both inputs
distance_premise = 500
speed_premise = 15

# extract all quantities as valid numbers (integers or floats)
distance_hypothesis = float(input("Enter the distance Sandy covers: "))
time_hypothesis = float(input("Enter the time Sandy takes to cover the distance: "))

# compare the defined variables
if distance_hypothesis > distance_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif time_hypothesis > time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
