# from PIL import Image

# img=Image.open('new.jpg')

# #transposing

# t=img.transpose(Image.FLIP_LEFT_RIGHT)

# #SAVE TO FILE

# t.save('new_new.jpg')

# print("Done Flipping")

#Image Enhancement
# import cv2


def print_matrix(rows, cols):
    num = 1
    for i in range(rows):
        for j in range(cols):
            print(num, end="\t")
            num += 1
        print()

row = 3
column = 3
print_matrix(row, column)
