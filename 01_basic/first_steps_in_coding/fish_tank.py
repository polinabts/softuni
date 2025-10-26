length = int (input())
width = int (input())
hight = int (input())
percent = float (input())

volume = length * width * hight
volume_dm = volume / 1000
volume_l = volume_dm - (volume_dm * (percent / 100))

print (float (volume_l))