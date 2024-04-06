# Premise: And for white males, there is almost a 40% chance they will have been arrested by 23, according to the report.
# Hypothesis: White males have a 40% risk of arrest by same age.
# Golden Label: neutral

arrest_chance_premise = 0.40
arrest_chance_hypothesis = 0.40

# the hypothesis mentions the arrest chance of white males by 23, which is also mentioned in the premise
if arrest_chance_hypothesis != arrest_chance_premise:
    # check if the arrest chance in the hypothesis contradicts the arrest chance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

