def classPhotos(redShirtHeights, blueShirtHeights):
   redShirtHeights.sort()
   blueShirtHeights.sort()

   if redShirtHeights[-1]<blueShirtHeights[-1]:
       front_row,back_row = redShirtHeights,blueShirtHeights
   else:
       front_row,back_row = blueShirtHeights,redShirtHeights

   return all(front<back for front,back in zip(front_row,back_row))


   
redShirtHeights =  [5, 8, 1, 3, 4]
blueShirtHeights =  [5, 9, 2, 4, 5]
classPhotos = classPhotos(redShirtHeights, blueShirtHeights)
print(classPhotos)