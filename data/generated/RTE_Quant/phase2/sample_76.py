# Premise: Monday, when the hearings begin, the Palestinians will hold their demonstration during the same hours, and a 25-person counter-demonstration by Israelis and Jews will take place.
# Hypothesis: Israelis will demonstrate and a counter-demonstration of 25 Palestinians will be permitted as well.
# Golden Label: neutral

# number of demonstrators in each group according to the premise
palestinians_premise = 25
israelis_premise = 25

# number of demonstrators in each group according to the hypothesis
palestinians_hypothesis = 25
israelis_hypothesis = 25

# the premise mentions a demonstration by Palestinians and a counter-demonstration by Israelis
# the hypothesis talks about a demonstration by Israelis and a counter-demonstration by Palestinians
# the two demonstrations being held are the same, but the groups holding them are switched between the premise and the hypothesis
# therefore, we need to compare the number of demonstrators in each group between the premise and the hypothesis

if (palestinians_premise != israelis_hypothesis) or (israelis_premise != palestinians_hypothesis):
    # if the number of demonstrators in either group contradicts between the premise and the hypothesis, we infer contradiction
    label = "contradiction"
else:
    # if the numbers match, we infer entailment
    label = "entailment"

print(label)

