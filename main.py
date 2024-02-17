import tkinter as tk
from pathlib import Path
from util import Util

class Gui(Util):
    def __init__(self, folderPath, saveFileName):
        super().__init__(saveFileName)
        self.root = tk.Tk()
        self.root.title("Image Similarity")

        self.folderPath = folderPath
        self.maxWidth = 300
        self.maxHeight = 300

        self.imageList = self.getImageDir()
        self.currentPairIndex = 0

        self.renderImages()
    def getImageDir(self):
        return list(map(str, Path(self.folderPath).glob('*.*')))

    def renderImages(self):
        self.image1Path = self.imageList[0]
        self.image2Path = self.imageList[1]

        tkImage1, tkImage2 = self.getTkImage(self.image1Path, self.image2Path)

        self.label1 = tk.Label(self.root, image=tkImage1)
        self.label1.grid(row=0, column=0)

        self.label2 = tk.Label(self.root, image=tkImage2)
        self.label2.grid(row=0, column=1)

        matchButton = tk.Button(self.root, text="match", command=self.match)
        matchButton.grid(row=1, column=0, columnspan=2)
        
        missMatchButton = tk.Button(self.root, text="miss match", command=self.missMatch)
        missMatchButton.grid(row=2, column=0, columnspan=2)

        self.root.mainloop()

if __name__ == "__main__":
    Gui("images/", "imageSimilarityDataset.csv")
