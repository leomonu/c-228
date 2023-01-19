from PIL import Image

def genData(data):

		newd = []

		for i in data:
			newd.append(format(ord(i), '08b'))
		return newd


def main():
	a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n"))
	if (a == 1):
		encode()

	elif (a == 2):
		print("Decoded Word : " + decode())
	else:
		raise Exception("Enter correct input")
	    
def modPix(pix, data):

	datalist = genData(data)
	lendata = len(datalist)
	imdata = iter(pix)

	for i in range(lendata):

		
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]]

		
		for j in range(0, 8):
			if (datalist[i][j] == '0' and pix[j]% 2 != 0):
				pix[j] -= 1

			elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
				if(pix[j] != 0):
					pix[j] -= 1
				else:
					pix[j] += 1
				# pix[j] -= 1

		
		if (i == lendata - 1):
			if (pix[-1] % 2 == 0):
				if(pix[-1] != 0):
					pix[-1] -= 1
				else:
					pix[-1] += 1

		else:
			if (pix[-1] % 2 != 0):
				pix[-1] -= 1

		pix = tuple(pix)
		yield pix[0:3]
		yield pix[3:6]
		yield pix[6:9]

def encode_enc(newimg, data):
    w=newimg.size[0]
    print("what is  w",w)

    (x, y) = (0, 0) 
    for i in modPix(newimg.getdata(), data):
        newimg.putpixel((x, y), i) 
        if(x == w-1):
            x = 0 
            y += 1 
        else: 
            x += 1









	

def encode():
    image=input("Enter the image name(with extenstion png format): ")
    image=Image.open(image)
    mymsg=input("Enter the msg u hve to hide:  ")
    if(len(mymsg)==0):
        raise ValueError("Msg is empty")
    
    myimage= image.copy()
    encode_enc(myimage,mymsg)

    newImage_with_hideMsg=input("Enter the name of new Image")
    myimage.save(newImage_with_hideMsg,str(newImage_with_hideMsg.split(".")[1].upper()))

    main()


def decode():
    image=input("Enter the image with hide name(with extenstion png format): ")
    image=Image.open(image)

    mymsg=""
    myimage=iter(image.getdata())

    while(True):
        pixel=[value for value in myimage.__next__()[:3]+
                                myimage.__next__()[:3]+
                                myimage.__next__()[:3]]
        binarystr=""
        for i in pixel[:8]:
            if(i%2==0):
                binarystr+="0"
            else:
                binarystr+="1"
        
        mymsg+=chr(int(binarystr,2))
        if (pixel[-1] % 2 != 0):
                return mymsg






















	

# Main Function


# Driver Code
if __name__ == '__main__' :

	# Calling main function
	main()