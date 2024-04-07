# Premise: List L:ABC, BCA, CAB In list L above, there are 3 positive integers, where each of A, B, and C is a different nonzero digit.
# Hypothesis: List L:ABC, BCA, CAB In list L above, there are less than 3 positive integers, where each of A, B, and C is a different nonzero digit.
# Golden Label: contradiction

integers_in_list_premise = 3
integers_in_list_hypothesis = 3

# the hypothesis talks about the number of positive integers in a list, referenced also in the premise
if integers_in_list_hypothesis >= integers_in_list_premise:
    # check if the hypothesis value contradicts the premise of less than 'integers_in_list_premise'
    label = "contradiction"
else:
    # the premise specifies the exact number of integers
    # any number less than 'integers_in_list_premise' cannot be explicitly inferred from the premise, hence it is neutral
    label = "neutral"

print(label)

