#cd C:\Users\quewa\Documents\pyzo\InterrogationNombre
import streamlit as st #streamlit run InterrogationNombre.py




st.title("Vérification des décimales de π")

pi = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"

string2 = st.text_input("Entrez les décimales de π que vous connaissez : ")

correct_decimals = 0

texte = ""
for i in range(min(len(pi), len(string2))):
    if pi[i] == string2[i]:
        texte += f"<span style='color:green '>{string2[i]}</span>"
        if not("red" in texte):
            correct_decimals += 1
    else:
        texte += f"<span style='color:red'>{string2[i]}</span>"

# Afficher le texte avec les balises HTML
st.markdown(texte, unsafe_allow_html=True)

st.write(f"Nombre de décimales correctes avant la première erreur : {correct_decimals}")



st.title("Vérification des décimales de e")

e="718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630"

string3 = st.text_input("Entrez les décimales de e que vous connaissez : ")

correct_decimals3 = 0

texte3 = ""
for i in range(min(len(e), len(string3))):
    if e[i] == string3[i]:
        texte3 += f"<span style='color:green '>{string3[i]}</span>"
        if not("red" in texte):
            correct_decimals3 += 1
    else:
        texte3 += f"<span style='color:red'>{string3[i]}</span>"

# Afficher le texte avec les balises HTML
st.markdown(texte3, unsafe_allow_html=True)

st.write(f"Nombre de décimales correctes avant la première erreur : {correct_decimals3}")


st.title("Vérification des décimales de φ")

phi="6180339887498948482045868343656381177203091798057628621354486227052604628189024497072072041893911374847540880753868917521266338622235369317931800607667263"

# Entrée utilisateur pour les décimales de φ
string4 = st.text_input("Entrez les décimales de φ que vous connaissez :")

correct_decimals4 = 0
texte4 = ""
for i in range(min(len(phi), len(string4))):
    if phi[i] == string4[i]:
        texte4 += f"<span style='color:green'>{string4[i]}</span>"
        if not("red" in texte):
            correct_decimals4 += 1
    else:
        texte4 += f"<span style='color:red'>{string4[i]}</span>"

# Afficher le texte avec les balises HTML
st.markdown(texte4, unsafe_allow_html=True)
st.write(f"Nombre de décimales correctes avant la première erreur : {correct_decimals4}")


st.title("Vérification des décimales de √2")

# Décimales connues de √2
sqrt2 = "4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727"
         

# Entrée utilisateur pour les décimales de √2
string5 = st.text_input("Entrez les décimales de √2 que vous connaissez :")

correct_decimals5 = 0
texte5 = ""
for i in range(min(len(sqrt2), len(string5))):
    if sqrt2[i] == string5[i]:
        texte5 += f"<span style='color:green'>{string5[i]}</span>"
        if not("red" in texte):
            correct_decimals5 += 1
    else:
        texte5 += f"<span style='color:red'>{string5[i]}</span>"

# Afficher le texte avec les balises HTML
st.markdown(texte5, unsafe_allow_html=True)
st.write(f"Nombre de décimales correctes avant la première erreur : {correct_decimals5}")


















