#Let's use the write mode and function
#1)"w"
am="jai shree ram"
f=open("meri_file.txt","w")
f.write(am)
f.close()

#if  we do the sam process with the same filename what willl hapen is UnicodeTranslateError
#the fie contenet will be overwrited and the new one will be added to the file.

#2)"r"
f=open("1.txt","r")
data=f.read()
print(data)
f.close()

#3)"r+" -> Reads and prints then writes the provoded content tot the same file.
with open("meri_file.txt","r+") as f:
    data=f.read()
    f.write("Mera  joota hai japani")


#4)"w+" ->Writes first and then reads the content in the file.
with open("meri_file.txt","w+") as f:
    f.write("Yeh desh hai veeer javanon ka")
    f.seek(0)
    data=f.read()
    print(data)

    #seek() is used to take the cursor to a specific positioon in the file.
    #seek(0) makes sure that thr cursor is at the 
    #starting of the file.


#5)"a" ->appends the data to the end of the file if thefilr exists
#but if the file doesnot exists it creates the file with the given content.

with open("meri.file.txt","a") as f:
    f.write("Jai hind")
    

#6)"a+" ->Both appending followed by reading.
with open("meri_file.txt","a+") as f:
    f.write("Main rahun ya na rahuun , mera desh hamesha rahega")
    f.seek(0)
    print(f.read())

#same is with binary files you just hab to add b with every mode.