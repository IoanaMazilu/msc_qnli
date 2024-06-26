premise_homeowners = 5500000
hypothesis_homeowners = 5500000
premise_words = 0
hypothesis_words = 0

# the hypothesis and premise mention the same number of homeowners and the same number of words in the closing documents
if premise_homeowners!= hypothesis_homeowners:
    # check if the number of homeowners in the hypothesis contradicts the number of homeowners in the premise
    label = "contradiction"
elif premise_words!= hypothesis_words:
    # check if the number of words in the hypothesis contradicts the number of words in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same number of homeowners and the same number of words in the closing documents
    label = "entailment"

print(label)
