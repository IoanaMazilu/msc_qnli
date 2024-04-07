# Premise: Sachin Tendulkar bough a red ferrari with a strange 5 digit numbered plate.
# Hypothesis: Sachin Tendulkar bough a red ferrari with a strange 6 digit numbered plate.
# Golden Label: contradiction

plate_number_digits_premise = 5
plate_number_digits_hypothesis = 6

# the hypothesis refers to the number of digits on the plate of Sachin's Ferrari, also mentioned in the premise
if plate_number_digits_premise != plate_number_digits_hypothesis:
    # check if the number of digits in the hypothesis contradicts the number of digits reported in the premise
    label = "contradiction"
else:
    # if the number of digits in the hypothesis does not contradict the number of digits in the premise, we can infer entailment
    label = "entailment"

print(label)

