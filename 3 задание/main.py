class MyFile:
    def __init__(self,name):
        self.count=0
        self.name=name
        self.text=[]
        with open(self.name, 'r', encoding='utf-8') as f:
            for line in f:
                self.count += 1
                self.text.append(line)
        for i in range(len(self.text)):
            self.text[i]=self.text[i].replace('\n','')

def task_3(Files):
    for file in Files:
        with open('test.txt', 'a', encoding='utf-8') as f:
            f.write(f'{Files[file].name}\n')
            f.write(f'{Files[file].count}\n')
            for el in Files[file].text:
                f.write(f'{el}\n')

file1 = MyFile('1.txt')
file2 = MyFile('2.txt')
file3 = MyFile('3.txt')
Files={len(file1.text):file1,len(file2.text):file2,len(file3.text):file3}
sorted_Files = dict(sorted(Files.items()))
task_3(sorted_Files)
