# Premise: In addition to the arrests in the New York area, police in Italy detained 77 people in connection with organized crime.
# Hypothesis: Police in Italy also make 77 arrests in connection with organized crime.
# Golden Label: entailment

arrests_italy_premise = 77
arrests_italy_hypothesis = 77

# the hypothesis mentions the number of arrests in Italy, which is also mentioned in the premise
if arrests_italy_hypothesis != arrests_italy_premise:
    # check if the number of arrests in Italy from the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of arrests in Italy from the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

