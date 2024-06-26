# Define variables for the numerical entities in the premise and hypothesis
members_club_premise_england = 26
members_club_premise_france = 26
members_club_premise_italy = 32

members_club_hypothesis_england = 86
members_club_hypothesis_france = 26
members_club_hypothesis_italy = 32

# Extract all quantities as valid numbers

# Check if the hypothesis values contradict the premise
if members_club_hypothesis_england <= members_club_premise_england:
    label = "contradiction"
elif members_club_hypothesis_france!= members_club_premise_france:
    label = "contradiction"
elif members_club_hypothesis_italy!= members_club_premise_italy:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
