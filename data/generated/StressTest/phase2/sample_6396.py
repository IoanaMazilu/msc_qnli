# Premise: In 1979 approximately 1/3 of the 32.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Hypothesis: In less than 6979 approximately 1/3 of the 32.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Golden Label: entailment

year_premise = 1979
year_hypothesis = 6979
passengers_premise = 32.3
passengers_hypothesis = 32.3

# the hypothesis refers to the same number of passengers as the premise, but in a different year
if year_hypothesis >= year_premise:
    # check if the hypothesis year contradicts the premise year
    label = "contradiction"
elif passengers_hypothesis != passengers_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

