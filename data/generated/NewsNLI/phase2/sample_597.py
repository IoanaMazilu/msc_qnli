# Premise: An investigation was launched into the Flight 370 matter, with Malaysian and aviation authorities reviewing video and other documentation to try to identify not only who the passengers were that used the stolen passports but how the illegal passports cleared security.
# Hypothesis: Two passengers on the missing Malaysian Airlines flight were traveling on stolen passports.
# Golden Label: neutral

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

