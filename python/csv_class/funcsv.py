class Fun_csv(object):
    
    def __init__(self, name):
        self.file_csv = name

    def data(self) : # a function for import data from a file csv
        x = []
        with open(self.file_csv) as file :
            y = file.read()
            y = list(y)
            for i in range(y.count("\n")) :
                z = y[0:y.index("\n")]
                x.append("".join(z)+";")
                y = y[y.index("\n")+1:len(y)]
            return x
        
    def data_vdf(self) : # Function to vertically organize data imported from csv file
        x = self.data()
        data_vdf_d = {x[0]:x[1:]}
        return data_vdf_d
    
    def data_hdf(self) : # The function horizontally organizes the data imported from the csv file
        x = self.data()
        data_hdf_d = {}
        for i in x :
            data_hdf_d[i[0:i.index(";")]]=i[i.index(";")+1:]
        return data_hdf_d
    
    def number_of(self,mode="c") : # for Counts the number of columns, rows and cells in a CSV file
        x = self.data()
        z = 0
        if mode == "c" :
            def cells_in_row(self, mode="r") :
                y = x[int(mode[1:])]
                if y[0] != ";" :
                    z = x[int(mode[1:])].count(";")
                else :
                    z = x[int(mode[1:])].count(";")-1
                return z
            for i in range(len(x)) :
                z += cells_in_row(self, mode=f"r{i}")
            return z
        elif  mode[0] == "r" :
            z = len(x)
        elif mode == "co" :
            z = len(data_hdf(fc))
        return z
    
    def csv_files_in(self, folder) :  # this function is to return the csv files in folder 
        import os
        list_folder = os.listdir(r"{}".format(folder))
        y = []
        for i in list_folder :
            x = i[-4:]
            if x == ".csv" :
                y.append(i)
        return y
    
    def creat_and_write(self,data="\n") : # This function is for create csv file and write  in it
        with open(r"{}".format(self.file_csv),mode="a") as file :
            file.write(data)
        print("created")
    
    def keyword(self,word) : # This function to receive a keyword and then search for the row it belongs to
        x = self.data()
        for i in x :
            if word in i :
                return i 
    
    def index_cell(self,cell) : # a function for return the place of cell in the file
        d = self.data()
        z = self.keyword(cell)
        y = d.index(z)+1
        x = z[0:z.index(cell)].count(";")+1
        return {"x":x,"y":y}
    
    def clear(self) : # a function for delete data in file csv
        with open(self.file_csv,mode="w") as file :
            pass
        
        


if __name__ == "__main__":
    
    fun_csv = Fun_csv(r"C:\Users\Administrator\Desktop\MyFolder\csv_class\funcsv_2.csv")
    print(fun_csv.data())
    print(fun_csv.data_vdf())
    print(fun_csv.data_hdf())
    print(fun_csv.number_of())
    print(fun_csv.csv_files_in(r"C:\Users\Administrator\Desktop\MyFolder\csv_class"))
    print(fun_csv.creat_and_write())
    print(fun_csv.keyword("rahimo"))
    print(fun_csv.index_cell("id"))
    #print(fun_csv.clear())