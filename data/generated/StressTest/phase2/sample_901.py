# Premise: If an outfit consists of less than 7 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Hypothesis: If an outfit consists of 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Golden Label: neutral

outfit_shirts_premise = 7
outfit_shirts_hypothesis = 1

# The hypothesis talks about the number of shirts used in an outfit, referenced also in the premise
if outfit_shirts_hypothesis >= outfit_shirts_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'outfit_shirts_premise'
    label = "contradiction"
elif outfit_shirts_hypothesis < outfit_shirts_premise:
    # Check if the hypothesis value is less than the 'outfit_shirts_premise'
    # If it is, then the hypothesis can be inferred from the premise
    label = "entailment"
else:
    # If the hypothesis value neither contradicts or can be inferred from the premise, then it is neutral. 
    label = "neutral"

print(label)

