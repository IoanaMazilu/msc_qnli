premise = "To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 760 members."
hypothesis = "To be considered for “ movie of the year, ” a film must appear in at least less than 4/4 of the top-10-movies lists submitted by the Cinematic Academy’s 760 members."

# extract the numerical entities from the premise and hypothesis
premise_num_lists = 760
premise_num_films = 1/4
hypothesis_num_lists = 760
hypothesis_num_films = 4/4

# compare the numerical entities
if hypothesis_num_films < premise_num_films:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif hypothesis_num_lists < premise_num_lists:
    # the hypothesis value is less than the premise value, but not contradictory
    label = "neutral"
else:
    # the hypothesis value is greater than or equal to the premise value, and does not contradict the premise
    label = "entailment"

print(label)
