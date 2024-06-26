# do not change the indentation level

# the premise and hypothesis mention the number of homeowners and the reduction of words in closing documents
if "2010" in hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif "words" in hypothesis:
    # check if the reduction of words in the hypothesis contradicts the premise estimate of less words
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of homeowners
    # any estimate of the number of homeowners in the hypothesis consistent with the premise is neutral
    label = "neutral"

print(label)
