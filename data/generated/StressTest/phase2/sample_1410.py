# Premise: Find by how much percentage Raj’s age is more than Hema’s when Raj will be 20 years old.
# Hypothesis: Find by how much percentage Raj’s age is more than Hema’s when Raj will be less than 30 years old.
# Golden Label: entailment

raj_age_premise = 20
raj_age_hypothesis = 30

# The hypothesis refers to a situation in which Raj's age is less than 'raj_age_hypothesis', also referenced in the premise
if raj_age_premise >= raj_age_hypothesis:
    # check if the premise value contradicts the hypothesis
    label = "contradiction"
else:
    # the hypothesis gives a broader range than the premise
    # Raj being 20 years old is consistent with him being less than 30 years old but cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)

