# Premise: In how many ways can you seat more than 1 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Hypothesis: In how many ways can you seat 7 people on a bench if one of them, Rohit, does not want to sit on the middle seat or at either end?
# Golden Label: neutral

people_seating_premise = 1
people_seating_hypothesis = 7

# both the hypothesis and premise refer to the number of people that can be seated on a bench with the condition of Rohit not wanting to sit in certain positions
if people_seating_premise >= people_seating_hypothesis:
    # check if the hypothesis value contradicts the premise estimate of more than 'people_seating_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people that can be seated
    # any number of people greater than 'people_seating_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
    
print(label)

