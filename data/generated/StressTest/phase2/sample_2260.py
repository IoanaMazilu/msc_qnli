# Premise: Jason is more than 1 times older than Bob at present.
# Hypothesis: Jason is 4 times older than Bob at present.
# Golden Label: neutral

jason_age_multiple_premise = 1
jason_age_multiple_hypothesis = 4

# the hypothesis refers to the relationship between Jason's and Bob's ages mentioned in the premise
if jason_age_multiple_hypothesis <= jason_age_multiple_premise:
    # check if the multiple of 'jason_age_multiple_hypothesis' contradicts the multiple of Jason's age in the premise
    label = "contradiction"
else:
    # the premise gives only a minimum multiple for Jason's age in relation to Bob's age
    # any multiple greater than 'jason_age_multiple_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

