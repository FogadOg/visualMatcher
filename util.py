from PIL import Image, ImageTk
import csv

class Util():
    def __init__(self, filename):
        self.filename=filename
        self.fields=["image1", "image2", "label"]
        self.writeHeaders()
    
    def writeHeaders(self):
        with open(self.filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fields)
            writer.writeheader()

    def writeRow(self, row):
        with open(self.filename, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fields)
            writer.writerow(row)


    def resizeImage(self, imagePath):
        image = Image.open(imagePath)
        width, height = image.size
        if width > self.maxWidth or height > self.maxHeight:
            ratio = min(self.maxWidth / width, self.maxHeight / height)
            newWidth = int(width * ratio)
            newHeight = int(height * ratio)
            return image.resize((newWidth, newHeight), Image.ANTIALIAS)
        else:
            return image
    
    def match(self):
        row = {
            "image1": self.image1Path,
            "image2": self.image2Path,
            "label": 1
        }
        self.writeRow(row)
        self.updateImages()

    def missMatch(self):
        row = {
            "image1": self.image1Path,
            "image2": self.image2Path,
            "label": 0
        }
        self.writeRow(row)
        self.updateImages()

    def updateImages(self):
        self.currentPairIndex = (self.currentPairIndex + 1) % (len(self.imageList) // 2)

        self.image1Path = self.imageList[self.currentPairIndex * 2]
        self.image2Path = self.imageList[self.currentPairIndex * 2 + 1]

        tkImage1, tkImage2 = self.getTkImage(self.image1Path, self.image2Path)

        self.label1.configure(image=tkImage1)
        self.label1.image = tkImage1
        self.label2.configure(image=tkImage2)
        self.label2.image = tkImage2

    def getTkImage(self, image1Path, image2Path):
        image1Resized = self.resizeImage(image1Path)
        image2Resized = self.resizeImage(image2Path)

        tkImage1 = ImageTk.PhotoImage(image1Resized)
        tkImage2 = ImageTk.PhotoImage(image2Resized)

        return tkImage1, tkImage2