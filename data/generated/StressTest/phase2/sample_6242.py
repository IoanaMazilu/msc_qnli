# Premise: If the ratio of area of triangle ADE to that of the trapezium DECB is 144:25 and BC = 13 cm, then find the length of DE.
# Hypothesis: If the ratio of area of triangle ADE to that of the trapezium DECB is 244:25 and BC = 13 cm, then find the length of DE.
# Golden Label: contradiction

ratio_triangle_to_trapezium_premise = 144/25
ratio_triangle_to_trapezium_hypothesis = 244/25
length_BC_premise = 13
length_BC_hypothesis = 13

# the hypothesis refers to the same ratio and length as the premise
if ratio_triangle_to_trapezium_premise != ratio_triangle_to_trapezium_hypothesis:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif length_BC_premise != length_BC_hypothesis:
    # check if the length of BC in the hypothesis contradicts the length of BC in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

