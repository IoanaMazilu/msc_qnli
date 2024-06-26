passengers_premise = 2
passengers_hypothesis = 2

# the premise mentions an investigation into the passengers that used stolen passports on Flight 370
# the hypothesis also mentions the two passengers with stolen passports on the missing flight
if passengers_hypothesis != passengers_premise:
    # check if the number of passengers from the hypothesis contradicts the number of passengers in the premise
    label = "contradiction"
else:
    # if the number of passengers in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
