# Premise: Three crew members and two passengers were taken to local hospitals.
# Hypothesis: There were 114 passengers and five crew members on board.
# Golden Label: neutral

crew_members_premise = 3
passengers_premise = 2
crew_members_hypothesis = 5
passengers_hypothesis = 114

# the hypothesis mentions the total number of passengers and crew members on board
# while the premise mentions the number of crew members and passengers taken to hospitals
# these sets of information are distinct and do not contradict each other
label = "neutral"

print(label)

