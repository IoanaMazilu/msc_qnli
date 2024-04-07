# Premise: If the ratio of their ages is 7:9, how old is Sandy?
# Hypothesis: If the ratio of their ages is 2:9, how old is Sandy?
# Golden Label: contradiction

# defining the ratios of their ages as per premise and hypothesis
age_ratio_premise = 7/9
age_ratio_hypothesis = 2/9

# comparing the ratios of their ages
if age_ratio_premise != age_ratio_hypothesis:
    label = "contradiction"
else:
    # no age value given, so no entailment possible
    label = "neutral"

print(label)

