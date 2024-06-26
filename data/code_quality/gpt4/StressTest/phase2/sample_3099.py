years_premise = 10
years_hypothesis = 30

# the hypothesis refers to the time after which Souju's father's age will be twice Tharak's age, also mentioned in the premise
if years_hypothesis <= years_premise:
    # check if the hypothesis value contradicts the time stated in the premise
    label = "contradiction"
elif years_hypothesis > years_premise:
    # the premise gives a specific time after which Souju's father's age will be twice Tharak's age
    # any time more than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
