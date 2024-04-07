# Premise: If the ratio of area of triangle ADE to that of the trapezium DECB is 144:25 and BC = 13 cm, then find the length of DE.
# Hypothesis: If the ratio of area of triangle ADE to that of the trapezium DECB is less than 544:25 and BC = 13 cm, then find the length of DE.
# Golden Label: entailment

ratio_premise = 144/25
ratio_hypothesis = 544/25
BC_premise = 13
BC_hypothesis = 13

# the hypothesis refers to the ratio of areas and the length of BC mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the estimate of 'ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
elif BC_hypothesis != BC_premise:
    # check if the length of BC in the hypothesis contradicts the length of BC reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

