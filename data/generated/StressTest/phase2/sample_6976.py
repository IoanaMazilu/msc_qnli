# Premise: If an outfit consists of less than 8 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Hypothesis: If an outfit consists of 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Golden Label: neutral

outfit_shirt_premise = 8
outfit_shirt_hypothesis = 1

# the hypothesis talks about the number of shirts in an outfit, also referenced in the premise
if outfit_shirt_hypothesis >= outfit_shirt_premise:
    # check if the hypothesis value contradicts the estimate of less than 'outfit_shirt_premise'
    label = "contradiction"
elif outfit_shirt_hypothesis < outfit_shirt_premise:
    # if the hypothesis value is less than the premise, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise, hence neutral
    label = "neutral"
    
print(label)

