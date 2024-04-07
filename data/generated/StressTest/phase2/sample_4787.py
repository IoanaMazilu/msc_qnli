# Premise: There are 25 stations between Hyderabad and Bangalore.
# Hypothesis: There are less than 25 stations between Hyderabad and Bangalore.
# Golden Label: contradiction

stations_premise = 25
stations_hypothesis = 25

# the hypothesis talks about the number of stations between Hyderabad and Bangalore, referenced also in the premise
if stations_hypothesis < stations_premise:
    # check if the hypothesis value contradicts the number of 'stations_premise'
    label = "contradiction"
elif stations_hypothesis == stations_premise:
    # if the number of stations in the hypothesis is equal to the number in the premise, we can infer entailment
    label = "entailment"
else:
    # any number of stations greater than 'stations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

