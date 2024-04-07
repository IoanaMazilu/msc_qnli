# Premise: In how many ways can you seat more than 1 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat 4 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: neutral

people_seating_premise = 1
people_seating_hypothesis = 4

# the hypothesis talks about the number of people you can seat on a bench, referenced also in the premise
if people_seating_hypothesis <= people_seating_premise:
    # check if the hypothesis value contradicts the estimate of more than 'people_seating_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people you can seat
    # any number of people greater than 'people_seating_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

