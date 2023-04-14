#O(nlogn)T|O(1)S
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    
    first_row_color = 'RED' if redShirtHeights[0]<blueShirtHeights[0] else 'BLUE'

    for idx in range(len(redShirtHeights)):
        red_height = redShirtHeights[idx]
        blue_height = blueShirtHeights[idx]
        if first_row_color == 'RED':
            if red_height >= blue_height:
                return False
        else:
            if blue_height >=red_height:
                return False
    return True

    
   
redShirtHeights =  [5, 8, 1, 3, 4]
blueShirtHeights =  [6, 9, 2, 4, 5]
classPhotos = classPhotos(redShirtHeights, blueShirtHeights)
print(classPhotos)