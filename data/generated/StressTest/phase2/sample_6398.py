# Premise: In 1979 approximately 1/3 of the 32.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Hypothesis: In 6979 approximately 1/3 of the 32.3 million airline passengers traveling to or from the United States used Kennedy Airport.
# Golden Label: contradiction

year_premise = 1979
year_hypothesis = 6979
passengers_premise = 32.3
passengers_hypothesis = 32.3
percentage_premise = 1/3
percentage_hypothesis = 1/3

# the hypothesis states the same facts as the premise, but for a different year
if year_premise != year_hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif passengers_premise != passengers_hypothesis:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
elif percentage_premise != percentage_hypothesis:
    # check if the percentage of passengers in the hypothesis contradicts the percentage of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

