def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if not fastest:
        redShirtSpeeds.sort(reverse=True)
    totalSpeed = 0
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds)-idx-1]
        totalSpeed += max(rider1,rider2)
    return totalSpeed





redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds =  [3, 6, 7, 2, 1]
fastest =  True
tandemBicycle = tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
print(tandemBicycle)

