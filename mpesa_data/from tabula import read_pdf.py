from tabula import read_pdf
import tabula

#df = read_pdf("/home/sibs/Documents/mpesa_data/testdata.pdf",pages ="all")

#print(data)
tabula.convert_into("/home/sibs/Documents/mpesa_data/testdata.pdf", "testdata.csv", output_format="csv", pages="all")

