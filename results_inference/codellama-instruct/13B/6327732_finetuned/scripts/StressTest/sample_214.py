# define variables for the numerical entities in the premise and hypothesis
average_speed_premise = 76
average_speed_hypothesis = 36
tom_speed_premise = 0
tom_speed_hypothesis = 0

# check if the hypothesis value contradicts the premise value
if average_speed_hypothesis <= average_speed_premise:
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
