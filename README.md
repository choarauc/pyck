# pyckpocket

Les données du projet se trouvent sous https://www.football-data.co.uk/downloadm.php.
Nous avons téléchargé les données au format csv pour les saisons 2015-2016 à 2021-2022.

Le dictionnaire de données du dataframe principal df_model est :

Index	Variable						Format		
0		Date							datetime64	
1		Equipe_domicile					object
2		Equipe_exterieur				object
3		But_match_equipe_domicile		int64
4		But_match_equipe_exterieur		int64
5		Resultat_match					object
6		But_mi_temps_equipe_domicile	int64
7		But_mi_temps_equipe_exterieur	int64
8		Resultat_mi_temps				object
9		Nb_tir_equipe_domicile			int64
10		Nb_tir_equipe_exterieur			int64
11		Nb_tir_cadre_equipe_domicile	int64
12		Nb_tir_cadre_equipe_exterieur	int64
13		Nb_fautes_equipe_domicile		int64
14		Nb_fautes_equipe_exterieur		int64
15		Corner_equipe_domicile			int64
16		Corner_equipe_exterieur			int64
17		Carton_jaune_equipe_domicile	int64
18		Carton_jaune_equipe_exterieur	int64
19		Carton_rouge_equipe_domicile	int64
20		Carton_rouge_equipe_exterieur	int64
21		Saison							object
22		Total_but_match					int64


Le dictionnaire de données du dataframe des côtes df_bookmakers_final est :
Index	Variable				Format			
0		Date					datetime64[ns]	
1		Equipe_domicile			object
2		Equipe_exterieur		object
3		Moy_cote_domicile		float64
4		Max_cote_domicile		float64
5		Moy_cote_exterieur		float64
6		Max_cote_exterieur		float64
7		Moy_cote_nul			float64
8		Max_cote_nul			float64
9		Saison					object

