# Premise: 15 years hence, Karthik will be just Quadrice as old as he was 15 years ago, How old is Karthik at now? [ Quadrice = 4 Times ].
# Hypothesis: less than 25 years hence, Karthik will be just Quadrice as old as he was 15 years ago, How old is Karthik at now? [ Quadrice = 4 Times ].
# Golden Label: entailment

years_hence_premise = 15
years_hence_hypothesis = 25
quadrice = 4
years_ago = 15

# the hypothesis refers to a point in time when Karthik's age will be quadrice the age he was 15 years ago
# both the premise and hypothesis are referring to the same event, but the time frames mentioned are different
if years_hence_hypothesis < years_hence_premise:
    # check if the time frame in the hypothesis contradicts the time frame given in the premise
    label = "contradiction"
else:
    # the premise gives only a specific time frame
    # any time frame greater than 'years_hence_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

