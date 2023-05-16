
def euler_p1(borne_sup):
	bun = borne_sup // 3 if borne_sup % 3 == 0 else borne_sup // 3 +1
	bdeux = borne_sup // 5 if borne_sup % 5 == 0 else borne_sup // 5 +1
	liste = [x*3 for x in range(1, bun)]
	liste2 = [x*5 for x in range(1, bdeux)]
	liste3 = list(set(liste + liste2))
	return sum(liste3)

def euler_p2():
	borne = 4000000
	liste = [1, 2]
	liste_paire = []
	for x in range(1, borne):
		y = sum(liste[-2:])
		if y >= borne:
			break
		liste.append(y)
		if y%2 == 0:
			liste_paire.append(y)
	return sum(liste_paire)