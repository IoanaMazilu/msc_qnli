# Premise: If the ratio of area of triangle ADE to that of the trapezium DECB is less than 544:25 and BC = 13 cm, then find the length of DE.
# Hypothesis: If the ratio of area of triangle ADE to that of the trapezium DECB is 144:25 and BC = 13 cm, then find the length of DE.
# Golden Label: neutral

ratio_premise = 544/25
ratio_hypothesis = 144/25
bc_premise = 13
bc_hypothesis = 13

# the hypothesis talks about the ratio of areas and the length of BC, which are also referenced in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the hypothesis ratio contradicts the estimate of less than 'ratio_premise'
    label = "contradiction"
elif bc_hypothesis != bc_premise:
    # check if the length of BC in the hypothesis contradicts the length of BC reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of areas
    # any ratio less than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

