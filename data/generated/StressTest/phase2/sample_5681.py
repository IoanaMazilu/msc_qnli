# Premise: In 6 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Hypothesis: In more than 6 years from now, Lyn the circus Lion will be exactly half as old as Ele, the circus Elephant.
# Golden Label: contradiction

years_future_premise = 6
years_future_hypothesis = 6

# the hypothesis refers to the same situation in the future as the premise
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis value contradicts the estimate of 'more than years_future_premise' years in the future
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years in the future
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

