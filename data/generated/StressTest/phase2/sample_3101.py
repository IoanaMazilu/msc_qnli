# Premise: Souju's father's age will be twice Tharak's age after 10 years.
# Hypothesis: Souju's father's age will be twice Tharak's age after more than 10 years.
# Golden Label: contradiction

years_premise = 10
years_hypothesis = 10

# the hypothesis is about the same event described in the premise
# but it refers to a period of time that is greater than the one in the premise
if years_hypothesis != years_premise:
    # check if the time period in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the time period in the hypothesis does not contradict the one in the premise
    # we can infer entailment
    label = "entailment"

print(label)

