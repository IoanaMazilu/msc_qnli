people_seating_premise = 2
people_seating_hypothesis = 9

# both hypothesis and premise talk about the number of people you can seat on a bench
if people_seating_hypothesis <= people_seating_premise:
    # check if the number of people in the hypothesis contradicts the premise's estimate of more than 'people_seating_premise' people
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_seating_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
