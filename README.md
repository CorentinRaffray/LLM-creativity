# LLM-creativity

## 1) Proposition d'un ensemble de métriques

Cette partie introduit le cadre théorique du problème de l'évaluation de la créativité des modèles de langage. Nous définissons théoriquement une mesure de la créativité et nous la comparons avec des annotations humaines.

## 2) Fiabilité des jugements humains
À partir des données de compar:IA, chaque session de vote est réalisée par un seul utilisateur qui compare simultanément deux modèles, il est donc impossible de mesurer l'accord inter-annotateurs au sens classique. De plus, seulement 30,9% des conversations reçoivent un vote. Les conversations votées sont systématiquement plus longues (+38% de tokens en médiane) et sur-représentent certaines thématiques engageantes (Environment, Food, Culture), au détriment des usages transactionnels courts.  
Le signal creative est donc bruité, en raison à la fois de la subjectivité du concept et de son taux de base très faible. De plus, tout classement construit sur ces votes (type Bradley-Terry) mesure la performance sur un sous-échantillon biaisé et va favoriser les réponses longues et les sujets engageants.

## 3) Classement par le modèle de Bradley-Terry
## 4) Biais systématique dans les données
## 5) Validité de construit
