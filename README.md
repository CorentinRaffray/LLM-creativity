# LLM-creativity

## 1) Proposition d'un ensemble de métriques

Cette partie introduit le cadre théorique du problème de l'évaluation de la créativité des modèles de langage. Nous y définissons une mesure de la créativité fondée sur des principes théoriques rigoureux, que nous confrontons ensuite à des annotations humaines afin d'en évaluer la pertinence. Les coefficients de pondération de cette métrique sont dans un premier temps déterminés analytiquement, en s'appuyant sur des arguments théoriques motivés. Afin de ne pas se limiter à cette seule justification formelle, nous procédons également à une validation empirique : une dizaine de combinaisons alternatives de coefficients ont été systématiquement testées et comparées, confirmant que le choix théorique initial se révèle être la configuration la plus judicieuse au regard des données.

## 2) Fiabilité des jugements humains
À partir des données de compar:IA, chaque session de vote est réalisée par un seul utilisateur qui compare simultanément deux modèles, il est donc impossible de mesurer l'accord inter-annotateurs au sens classique. De plus, seulement 30,9% des conversations reçoivent un vote. Les conversations votées sont systématiquement plus longues (+38% de tokens en médiane) et sur-représentent certaines thématiques engageantes (Environment, Food, Culture), au détriment des usages transactionnels courts.  
Le signal creative est donc bruité, en raison à la fois de la subjectivité du concept et de son taux de base très faible. De plus, tout classement construit sur ces votes (type Bradley-Terry) mesure la performance sur un sous-échantillon biaisé et va favoriser les réponses longues et les sujets engageants.

## 3) Classement par le modèle de Bradley-Terry

Dans cette partie,on construit un classement des modèles à partir de comparaisons par paires en utilisant le modèle de Bradley-Terry. Le score de chaque modèle est estimé à partir des duels gagnés/perdus, d'abord sur l'ensemble global des votes (hors ex-aequo), puis sur le sous-ensemble ciblé "créativité". On retient un seuil minimal de confrontations (`N=30`) pour limiter l'instabilité liée aux modèles trop peu observés.

La comparaison entre classement global et classement créativité montre une forte cohérence générale, mais aussi des déplacements de rang qui indiquent que certains modèles sont relativement plus performants sur les prompts créatifs que sur l'usage moyen (et vis-versa). Puis on étudie l'effet des ex-aequo avec une extension de Davidson.

Enfin, une version enrichie du modèle avec covariables (longueur, catégorie, nombre de tours) confirme qu'une partie des écarts observés dépend du contexte d'évaluation. Certaines catégories ont une importance anormale mais en regardant de plus près elles sont très largement sous représentées (quelques votes seulement).



## 4) Biais systématique dans les données
Nous nous sommes par la suite intéressés aux éventuels biais qui pourraient expliquer des déséquilibres dans le choix du modèle favori par l'utilisateur, ou des biais qui pourraient entrainer davantage de réactions. En particulier, nous avons étudié le biais de longueur, c'est à dire, vérifier si la longueur de la conversation guide le choix de l'utilisateur, et nous avons également étudié le biais de position, afin de déterminer si la position dans laquelle la conversation était présentée à l'utilisateur engendrait une différence dans les réactions reçues. 
Dans le cas du biais de longueur, il est apparu que seule une très faible corrélation existait, une conversation plus longue de 100 tokens a seulement 2% de chance supplémentaire d'être choisie. 
La position ne reflète aucun biais en particulier. 
Nous avons également réfléchi à un protocole qui pourrait permettre de réduire ces biais. Par exemple en mettant en place sur l'interface un bouton "voir plus" pour que l'utilisateur découvre la conversation au fur et à mesure et soit moins influencé par sa longueur. Les paires de modèles mises en compétition pourraient également être choisies pour 70% d'entre elles de sorte à déterminer la position dans le classement de Bradley-Terry des modèles encore classés de manière incertaine, et pour le reste de manière uniforme pour s'assurer que l'ensemble des modèles soit bien représenté.

## 5) Validité de construit

Finalement nous avons voulu répondre à la question : Est ce que le label `creative` est un indicateur valide de créativité ? Par validité convergente, nous avons calculé que les corrélations entre le label `creative` et différentes métriques de créativité convergente sont positives mais très faibles (r < 0.4), indiquant que les métriques automatiques supposées de créativité ne capturent pas les mêmes choses que le label jugé par les utilisateurs. En particulier, il est peu lié à la diversité lexicale, à la rareté statistique, à l’éloignement sémantique ou à la longueur des réponses.
Par validité divergente, nous avons calculé que les corrélations entre le label `creative` et différentes métriques telles que la longueur des réponses, le format, la complétude ou encore l'exactitude sont également faibles (r < 0.15), ce qui est rassurant car cela indique que les utilisateurs ne confondent pas créativité et qualité générale. 

Ces résultats suggèrent que le label `creative` mesure une perception subjective de la créativité plutôt que des caractéristiques textuelles objectives. Le recours à un panel grand public renforce la validité écologique, mais introduit également une hétérogénéité des jugements. Une combinaison d’évaluations grand public et expertes permettrait ainsi d’obtenir une mesure plus robuste de la créativité.
