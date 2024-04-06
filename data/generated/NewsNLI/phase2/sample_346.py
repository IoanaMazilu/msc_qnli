# Premise: According to the statement, 281 of the 3,050 passengers and 22 of 1,165 crew members of Explorer of the Seas reported vomiting and diarrhea.
# Hypothesis: 281 passengers and 22 crew on Explorer of the Seas report gastrointestinal problems.
# Golden Label: entailment

passengers_total_premise = 3050
passengers_sick_premise = 281
crew_total_premise = 1165
crew_sick_premise = 22

passengers_sick_hypothesis = 281
crew_sick_hypothesis = 22

# the hypothesis mentions the number of passengers and crew members who reported sickness, which are also mentioned in the premise
if passengers_sick_hypothesis != passengers_sick_premise:
    # check if the number of sick passengers in the hypothesis contradicts the number of sick passengers reported in the premise
    label = "contradiction"
elif crew_sick_hypothesis != crew_sick_premise:
    # check if the number of sick crew members from the hypothesis contradicts the number of sick crew members in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

