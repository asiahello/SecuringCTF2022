list_constellation = []
with open("constellations.txt") as constellation:
	for line in constellation:
		line = line[1:-2]
		list_constellation.append(line)

sky_road = []
with open("skymap.txt") as skymap:
	line = skymap.readlines()[0]	
	for i in range(len(line)//8):
		sky_road.append(line[i*8:(i+1)*8])


decoded_ascii = ""
hex_ascii=''
for path in sky_road:
	hex_ascii += chr(list_constellation.index(path))
	if len(hex_ascii) == 2:
		decoded_ascii += bytes.fromhex(hex_ascii).decode("ASCII")
		hex_ascii=''
		
print(decoded_ascii)
