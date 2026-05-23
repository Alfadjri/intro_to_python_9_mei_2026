#int
# integer adalah angka bulat
x = 32767
print("Contoh bilangan integer (int) : {0}".format(x))
# float
# float bilangan desimal
y = 9.8
print("Contoh bilangan float (float) : {0}".format(y))
# complex
# complex nilai formula
z = 3 + 2j
print("Contoh bilangan complex (complex) : {0}".format(z))

#sqyencial type
# list
# list sifat tipe data yang harus sama semua tidak boleh beda
a = [1,2,3,4,5,6]
print("Contoh tipe data list (list) : {0}".format(a))
# truplet
# truplet sifat tipe data tidak bisa di ubah atau final
b = (1,2,3,4,5)
print("Contoh tipe data truplet (truplet) : {0}".format(b))
# range
# range sifat tipe data berurutan
c = range(1,5)
print("Contoh tipe data range (range) : {0}".format(c))

# Text
# String
# String Tulisan atau text
nama = "Alfadjri Dwi F"
print("Contoh tipe data String (String) : {0}".format(nama))

# Maping
# Dictionary
# Dictionary tipe data seperti profile
profile = { "nama" : nama , "age": 25}
print("Contoh tipe data Dictionary (dict) : {0}".format(profile["nama"]))

# Set
# Set
# Set tipe data yang tidak bisa di ubah 
type_set = {1,2,3,4,5}
print("Contoh tipe data Set (Set) : {0}".format(type_set))
# frozenset
# frozenset
# frozenset tipe data yang tidak bisa di ubah di pertengahan atau set data 
type_frozenset = frozenset(a)
print("Contoh tipe data frozenset (frozenset) : {0}".format(type_frozenset))

# Boolean
# boolean
# boolean tipe data untuk kondisi dimana True(1) or False(0)
boolean = True
print("Contoh tipe data boolean (bool) : {0}".format(boolean))

# binary
# binary tipe data bit
binary = 0b01000010
# tidak baik 
# desimal = int(binary) #casting atau conversi int(nilaiyangmaudiubahkeinteger)
# karakter = chr(desimal)
karakter=chr(int(binary))
print("Contoh tipe data binary (binary) : {0}".format(karakter))

# biteArray
# biteArray
# biteArray tipe data yang menunjukan isi di dalam list dalam bentuk binary 
type_biteArray = bytearray(a)
print("Contoh tipe data biteArray (biteArray) : {0}".format(type_biteArray))
# memoryView
# memoryView
# memoryView tipe data yang menunjukan lokasi di dalam ram 
type_memoryView = memoryview(type_biteArray)
print("Contoh tipe data memoryView (memoryView) : {0}".format(type_memoryView))
