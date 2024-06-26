# define all the numbers in both premise and hypothesis
premise_numbers = [121, 144, 169, 196, 225, 256, 288, 324, 361]
hypothesis_numbers = [321, 144, 169, 196, 225, 256, 288, 324, 361]

# comparing the first number in hypothesis to the corresponding number in premise
if hypothesis_numbers[0] >= premise_numbers[0]:
    label = "contradiction"
else:
    # comparing the remaining numbers in both lists
    if premise_numbers[1:] == hypothesis_numbers[1:]:
        label = "entailment"
    else:
        label = "contradiction"

print(label)
