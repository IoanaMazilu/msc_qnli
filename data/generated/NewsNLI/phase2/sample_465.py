# Premise: The amount of outstanding fines range from 10,000 yuan ($1,600) up to 29 million yuan ($4.5 million).
# Hypothesis: The amount of outstanding fines listed are up to $4.5 million.
# Golden Label: entailment

fine_low_end_premise = 10000  # yuan
fine_high_end_premise = 29000000  # yuan
fine_low_end_premise_dollar = 1600  # dollars
fine_high_end_premise_dollar = 4500000  # dollars

fine_high_end_hypothesis_dollar = 4500000  # dollars

# the hypothesis mentions the high end of the range for the outstanding fines, which is also mentioned in the premise
if fine_high_end_hypothesis_dollar != fine_high_end_premise_dollar:
    # check if the high end fine in dollar from the hypothesis contradicts the high end fine in dollar reported in the premise
    label = "contradiction"
else:
    # if the high end fine in dollar from the hypothesis does not contradict the high end fine in dollar from the premise, we can infer entailment
    label = "entailment"

print(label)

