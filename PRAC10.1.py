#  PRANAY PATEL, 20CE098
from fpdf import FPDF


pdf = FPDF()


pdf.add_page()

pdf.set_font("Arial",size = 15)


print("\n-----------------------3rd Sem Result-----------------------\n")


Id = input("Enter your id : ")


print("\n\n              Subject Details                  \n")

print("CE244     : Software Group Project-1")

print("CE251     : Java Programming")

print("CE252     : Digital Electronics")

print("CE257     : Data Communication & Networking")

print("CA224  : Introduction To Web Designing")

print("HS121.02A : Creativity,Problem Solving and Innovation")

print("MA253     : Discrete Mathematics and Algebra\n")


Total_Credits = input("\nEnter Total Credits : ")


C_SGP = input("\nEnter Credit of CE244 : ")

SGP = input("Enter Grade of CE244 : ")


C_JAVA_T = input("\nEnter Credit of CE251-Theory : ")

JAVA_T = input("Enter Grade of CE251-Theory : ")


C_JAVA_P = input("\nEnter Credit of CE251-Practical : ")

JAVA_P = input("Enter Grade of CE251-Practical : ")


C_DE_T = input("\nEnter Credit of CE252-Theory : ")

DE_T = input("Enter Grade of CE252-Theory : ")

C_DE_P = input("\nEnter Credit of CE252-Practical : ")

DE_P = input("Enter Grade of CE252-Practical : ")


C_DCN_T = input("\nEnter Credit of CE257-Theory : ")

DCN_T = input("Enter Grade of CE257-Theory : ")

C_DCN_P = input("\nEnter Credit of CE257-Practical : ")

DCN_P = input("Enter Grade of CE257-Practical : ")


C_ARP = input("\nEnter Credit of CE281.01 : ")

ARP = input("Enter Grade of CE281.01 : ")


C_CPI = input("\nEnter Credit of HS121.02A : ")

CPI = input("Enter Grade of HS121.02A : ")


C_DMA = input("\nEnter Credit of MA253 : ")

DMA = input("Enter Grade of MA253 : ")


SGPA = input("\nEnter your SGPA : ")

Credits_Earned = int(C_SGP) + int(C_JAVA_T) + int(C_JAVA_P) + int(C_DE_T) + int(C_DE_P) + int(C_DCN_T) + int(C_DCN_P) + int(C_ARP) + int(C_CPI) + int(C_DMA)

print("")



pdf.cell(200, 10, txt = "", ln = 1, align = 'C')

pdf.cell(200,10,txt = f"          ID                      {Id}" ,ln=1,align='L')


pdf.cell(200, 10, txt = "", ln = 1, align = 'C')

pdf.cell(200, 10, txt = "", ln = 1, align = 'C')

pdf.cell(200,10,txt ="RESULT ",ln=1,align='C')

pdf.cell(200, 10, txt = "", ln = 1, align = 'C')



pdf.cell(200,10,txt =" Course Code                 Course Type                  Credit                  Grade ",ln=1,align='C')

pdf.cell(200,10,txt =f"   CE244                          Practical                         {C_SGP}                        {SGP} ",ln=1,align='C')

pdf.cell(200,10,txt =f"   CE25                            Theory                           {C_JAVA_T}                        {JAVA_T} ",ln=1,align='C')

pdf.cell(200,10,txt =f"   CE251                          Practical                         {C_JAVA_P}                        {JAVA_P} ",ln=1,align='C')

pdf.cell(200,10,txt =f"   CE252                           Theory                           {C_DE_T}                        {DE_T} ",ln=1,align='C')

pdf.cell(200,10,txt =f"   CE252                          Practical                         {C_DE_P}                        {DE_P} ",ln=1,align='C')

pdf.cell(200,10,txt =f"   CE257                           Theory                           {C_DCN_T}                        {DCN_T} ",ln=1,align='C')

pdf.cell(200,10,txt =f"   CE257                          Practical                         {C_DCN_P}                        {DCN_P} ",ln=1,align='C')

pdf.cell(200,10,txt =f" CE281.01                       Practical                         {C_ARP}                        {ARP} ",ln=1,align='C')

pdf.cell(200,10,txt =f"HS121.02 A                     Practical                         {C_CPI}                        {CPI} ",ln=1,align='C')

pdf.cell(200,10,txt =f"   MA253                           Theory                           {C_DMA}                        {DMA} ",ln=1,align='C')



pdf.cell(200, 10, txt = "", ln = 1, align = 'C')

pdf.cell(200, 10, txt = "", ln = 1, align = 'C')

pdf.cell(200,10,txt =" SEMESTER AVERAGE",ln=1,align='C')

pdf.cell(200, 10, txt = "", ln = 1, align = 'C')


pdf.cell(200,10,txt ="Total Credits                              Credits Earned                              SGPA    ",ln=1,align='C')

pdf.cell(200,10,txt =f"  {Total_Credits}                                                {Credits_Earned}                                          {SGPA}",ln=1,align='C')



pdf.cell(200, 10, txt = "", ln = 1, align = 'C')

pdf.output("20ce098_Pranay_Sem3_Result.pdf")