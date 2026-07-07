# ESPHome E-Ink Designer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/Interface-Tkinter-orange)
![ESPHome](https://img.shields.io/badge/ESPHome-Compatible-green)

## Présentation

**ESPHome E-Ink Designer** est un éditeur graphique permettant de créer des interfaces pour écrans E-Ink utilisés avec ESPHome.

Le but du projet est de permettre la conception visuelle d'un écran sans devoir écrire manuellement tout le code d'affichage ESPHome.

L'utilisateur place des éléments graphiques sur un écran virtuel, modifie leurs propriétés, puis génère automatiquement le code ESPHome correspondant.

---

# Fonctionnalités

## Éditeur graphique

- Canvas E-Ink virtuel
- Grille de placement
- Interface sombre moderne
- Sélection des objets
- Déplacement à la souris
- Suppression clavier
- Aperçu du code généré

---

## Objets disponibles

### Texte

Permet d'afficher du texte ou des valeurs dynamiques ESPHome.

Paramètres :

- Position X/Y
- Police ESPHome
- Alignement
- Valeur affichée

Exemple généré :

```cpp
it.print(
    20,
    30,
    id(font_value),
    TextAlign::TOP_LEFT,
    "Bonjour"
);
```

---

### Image

Permet d'afficher une image ESPHome.

Paramètres :

- Position X/Y
- Identifiant image ESPHome

Exemple :

```cpp
it.image(
    100,
    50,
    id(icon_temp)
);
```

---

### Rectangle

Permet de créer des formes simples.

Paramètres :

- Position
- Largeur
- Hauteur

Exemple :

```cpp
it.rectangle(
    10,
    10,
    50,
    30,
    COLOR_ON
);
```

---

# Interface

L'application est organisée comme un logiciel de conception graphique :

```
+------------------------------------------------+
| ESPHome E-Ink Designer                         |
|------------------------------------------------|
| Outils                                         |
|------------------------------------------------|
|                                                |
|       Canvas E-Ink       Propriétés            |
|                                                |
|                                                |
|------------------------------------------------|
| Code ESPHome                                   |
+------------------------------------------------+
```

---

# Installation

## Pré-requis

- Python 3.10 ou supérieur
- Tkinter installé

Vérifier Python :

```bash
python --version
```

---

## Lancement

Télécharger le projet :

```bash
git clone https://github.com/votre-compte/esphome-eink-designer.git
```

Entrer dans le dossier :

```bash
cd esphome-eink-designer
```

Lancer :

```bash
python main.py
```

---

# Structure du projet

```
ESPHome E-Ink Designer/

│
├── main.py
├── app.py
│
├── canvas.py
├── toolbar.py
├── properties.py
├── style.py
│
├── objects.py
├── generator.py
│
├── project.py
├── history.py
├── export.py
├── menu.py
│
├── projects/
│
└── exports/
```

---

# Description des fichiers

## app.py

Gestion principale :

- création de la fenêtre
- chargement des modules
- gestion des objets


## canvas.py

Gestion du designer :

- affichage E-Ink
- création d'objets
- sélection
- déplacement
- suppression


## objects.py

Définition des objets :

- TextObject
- ImageObject
- RectangleObject


## generator.py

Transforme les objets graphiques en code ESPHome.


## project.py

Gestion des projets :

- sauvegarde JSON
- chargement


## history.py

Gestion :

- Undo
- Redo


## export.py

Export des fichiers générés :

- YAML ESPHome
- Texte brut


## menu.py

Gestion du menu :

- Nouveau projet
- Sauvegarde
- Export
- Historique

---

# Sauvegarde des projets

Les projets sont sauvegardés dans :

```
projects/
```

Format :

```
mon_ecran.json
```

Exemple :

```json
[
    {
        "type": "text",
        "x": 20,
        "y": 30,
        "value": "Température"
    }
]
```

---

# Export ESPHome

Les fichiers générés sont placés dans :

```
exports/
```

Exemple :

```
screen_lambda.yaml
```

Résultat :

```yaml
lambda: |-
  it.print(
    20,
    30,
    id(font_value),
    TextAlign::TOP_LEFT,
    "Température"
  );
```

---

# Raccourcis clavier

| Action | Touche |
|---|---|
| Supprimer un objet | Suppr |
| Supprimer un objet | Backspace |

---

# Technologies utilisées

## Python

Langage principal du projet.

https://www.python.org/


## Tkinter

Bibliothèque graphique utilisée pour l'interface.


## ESPHome

Plateforme de génération et gestion des appareils ESP.

https://esphome.io/

---

# Roadmap

## Terminé

- [x] Interface graphique
- [x] Canvas E-Ink
- [x] Texte
- [x] Images
- [x] Génération ESPHome
- [x] Sauvegarde projet
- [x] Export
- [x] Menu application


## À venir

- [ ] Redimensionnement des objets
- [ ] Copier / coller
- [ ] Bibliothèque d'icônes
- [ ] Ajout de capteurs ESPHome
- [ ] Graphiques
- [ ] Aperçu E-Ink réaliste
- [ ] Export YAML ESPHome complet
- [ ] Gestion automatique des fonts
- [ ] Import d'images


---

# Contribution

Les améliorations sont les bienvenues.

Pour contribuer :

1. Créer une branche :

```bash
git checkout -b nouvelle-fonction
```

2. Modifier le projet

3. Envoyer une Pull Request


---

# Licence

Projet open-source.

Utilisation et modification autorisées selon la licence choisie pour le dépôt.


---

# Auteur

ESPHome E-Ink Designer

Développé avec :

- Python
- Tkinter
- ESPHome
