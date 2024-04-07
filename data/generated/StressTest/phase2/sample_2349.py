# Premise: At a certain automobile dealership that sells only Tajima's and Franks, the number of non hybrid Tajima's is 35 less than 3 times the number of hybrid Tajima's.
# Hypothesis: At a certain automobile dealership that sells only Tajima's and Franks, the number of non hybrid Tajima's is less than 65 less than 3 times the number of hybrid Tajima's.
# Golden Label: entailment

hybrid_tajimas_premise = 1  # The exact number is not given, so we set a representative variable
non_hybrid_tajimas_premise = 3 * hybrid_tajimas_premise - 35

hybrid_tajimas_hypothesis = 1  # The exact number is not given, so we set a representative variable
non_hybrid_tajimas_hypothesis = 3 * hybrid_tajimas_hypothesis - 65

# the hypothesis talks about the same dealership and the same categories of cars referenced in the premise
if non_hybrid_tajimas_hypothesis >= non_hybrid_tajimas_premise:
    # check if the hypothesis value contradicts the number of non hybrid Tajima's cars calculated in the premise
    label = "contradiction"
else:
    # the premise gives an exact formula for the number of non hybrid Tajima's cars
    # any number of non hybrid Tajima's cars less than the one calculated in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

