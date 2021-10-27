'''
def commaize(number):
    text = str(number)
    parts = text.split(".")
    ret = ""
    if len(parts) > 1:
        ret = "."
        ret += parts[1] # Apparently commas aren't used to the right of the decimal point
    # The -1 offsets to len() and 0 are because len() is 1 based but text[] is 0 based
    for i in range(len(parts[0]) - 1,-1,-1):
        # We can't just check (i % 3) because we're counting from right to left
        #  and i is counting from left to right. We can overcome this by checking
        #  len() - i, although it needs to be adjusted for the off-by-one with a -1
        # We also make sure we aren't at the far-right (len() - 1) so we don't end
        #  with a comma
        if (len(parts[0]) - i - 1) % 3 == 0 and i != len(parts[0]) - 1:
            ret = "," + ret
        ret = parts[0][i] + ret
    return ret
def main():
    number =input()
    print(commaize(number))
 '''


val= int(input())
print (format (val, ',d'))
print ('{:,}'.format(val)) 

# Hàm format() được tích hợp sẵn trong Python sử dụng để định dạng một giá trị truyền vào thành một định dạng cụ thể.
