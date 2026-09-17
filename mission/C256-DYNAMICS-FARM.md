# CEREBRON OMEGA — COLLATZ C256-C265 — DYNAMICS FARM

## Mission
Étudier exclusivement la dynamique globale et first-return de l'application accélérée de Collatz sur les impairs positifs.

## Checkpoint vérifié
T(x)=(3x+1)/2^{v2(3x+1)}.
Pour un mot de valuations a_0,...,a_{n-1}, A_k=sum_{i<k} a_i,
2^{A_k}x_k=3^k x_0+C_k, C_0=0, C_{k+1}=3C_k+2^{A_k}.
Les mots finis sont localement réalisables; cela ne prouve pas cycle ni first-return.
Les profils mécaniques quasi critiques peuvent rester multiplicativement proches de 1 arbitrairement longtemps.
Une fenêtre archimédienne de largeur c_W X+O(1), c_W>0, finit par rencontrer toute classe résiduelle fixe modulo 2^{A_n+1}.
La structure mécanique est liée aux rotations irrationnelles/Sturmian return words.
Le verrou global reste OPEN.

## Objectif unique
Déterminer si des épisodes FIRST-RETURN réellement admissibles de longueur arbitraire peuvent exister avec largeur normalisée positive, en tenant compte de tout le profil affine et non du seul produit final.

## Sous-tâches
1. Définir exactement entrée, première sortie, séjour extérieur et première réentrée dans I_X=[X,2X).
2. Écrire les contraintes simultanées sur x_0 pour tous les préfixes.
3. Étudier la durée maximale d'une excursion quand les multiplicateurs partiels suivent un profil équilibré/Sturmien.
4. Tester l'existence d'un UNIFORM ARC GAP dans la représentation par rotation.
5. Chercher des familles quasi tangentielles où le complément d'arc tend vers 0.
6. Étudier les opérateurs de régénération entre entrées successives dans une bande.
7. Séparer rigoureusement existence locale de mots, existence d'épisodes, cycle et trajectoire divergente.
8. Rechercher un invariant non recyclable lors des sorties/réentrées.
9. Falsifier toute prétendue contraction uniforme par construction explicite si possible.
10. Ne jamais conclure CYCLES CLOSED sans contradiction arbitraire-N complète.

## Sortie attendue
LEMMES PROUVÉS; CONTRE-EXEMPLES; BORNES DE TEMPS DE RETOUR; ARC GAP; FENÊTRE FIRST-RETURN; RÉGÉNÉRATION; GAPS; NEXTLOCK UNIQUE; VERDICT CYCLES OPEN/CLOSED.
