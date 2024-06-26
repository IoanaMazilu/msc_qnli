distance_walked_by_joke_paul_premise = 24
distance_walked_by_joke_paul_hypothesis = 24

# the hypothesis talks about the distance walked by Joke and Paul, referenced also in the premise
if distance_walked_by_joke_paul_hypothesis <= distance_walked_by_joke_paul_premise:
    # check if the hypothesis value contradicts the estimate of 'distance_walked_by_joke_paul_premise'
    label = "contradiction"
else:
    # the premise gives an exact distance walked by Joke and Paul
    # any distance greater than 'distance_walked_by_joke_paul_premise' contradicts the premise
    label = "contradiction"

print(label)
