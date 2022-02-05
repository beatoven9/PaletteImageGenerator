from PIL import Image, ImageColor
import sys

def parsePaletteFile(fileName):
    paletteList = []
    with open(fileName, 'r') as f:
        newPalette = []
        for line in f.readlines():
            if line[0] == "*" and len(newPalette) > 0:
                print("Label:", line[1:-1])
                paletteList.append(newPalette)
                newPalette = []
            elif line[0] == "-":
                colorStartIndex = line.index(":") + 2
                colorEndIndex = line.index(";")
                newColor = line[colorStartIndex:colorEndIndex]
                newPalette.append(newColor)
            elif line[0] == "#":
                continue
            else:
                continue
        paletteList.append(newPalette)

    return paletteList


def getPalettes():
    argc = len(sys.argv)
    argv = sys.argv

    paletteList = parsePaletteFile(argv[1]) 
    return paletteList

def createPaletteImage(colors):
    img = Image.new(mode="RGB", size=(16, len(colors)))
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i,j] = ImageColor.getrgb(colors[j])

    return img

def main():
    imgList = []
    palettes = getPalettes()
    for i in range(len(palettes)):
        imgList.append(createPaletteImage(palettes[i]))

    for i in range(len(imgList)):
        imgList[i].show()

if __name__ == "__main__":
    main()
