# Focusly 📋✨

> **Organise. Priorise. Accomplis.**

**Focusly** est une application mobile moderne de gestion de tâches développée avec **Python, Kivy et KivyMD**.

Elle permet de créer des tâches, leur attribuer une date et une heure, ajouter des notes, suivre les tâches en cours et consulter les tâches terminées.

---

## 📱 Aperçu

Focusly a été conçu pour proposer une interface simple et moderne permettant de gérer ses activités quotidiennes directement depuis son téléphone.

### Fonctionnalités principales

- ✅ Création de nouvelles tâches
- 📅 Sélection d'une date
- ⏰ Sélection d'une heure
- 📝 Ajout d'une note à une tâche
- ✔️ Marquage d'une tâche comme terminée
- 📋 Liste des tâches terminées
- 💾 Sauvegarde locale des tâches
- 🔄 Chargement automatique des tâches au démarrage
- ✨ Animation lors de l'ajout d'une nouvelle tâche
- 📱 Interface adaptée à une application mobile
- 🌙 Interface sombre moderne
- 💜 Identité visuelle Focusly

Les tâches sont enregistrées localement dans des fichiers JSON afin de conserver les données entre les lancements de l'application. 
---

## 🖥️ Interface

L'application est organisée autour de trois espaces principaux :

### 🏠 Accueil

Le tableau de bord affiche les tâches actuellement à réaliser.

Chaque tâche peut afficher :

- son nom ;
- une note ;
- sa date ;
- son heure ;
- une action permettant de la terminer.

### ➕ Ajouter

L'utilisateur peut créer une nouvelle tâche avec :

- **Nom de la tâche**
- **Date**
- **Heure**
- **Note**

La date et l'heure sont sélectionnées à l'aide des composants `MDDatePicker` et `MDTimePicker`.

### ✅ Tâches terminées

Lorsqu'une tâche est terminée, elle est retirée de la liste active et ajoutée à l'historique des tâches terminées avec sa date, son heure et sa description.

---

## 🛠️ Technologies utilisées

- 🐍 **Python**
- 🎨 **Kivy**
- 💎 **KivyMD**
- 📄 **KV Language**
- 💾 **JSON**
- 📱 Android — objectif principal du projet

---

## 📂 Structure du projet

```text
Focusly/
│
├── todo.py
├── todo_main.kv
├── task_end.kv
│
├── app_icon.png
├── check_icon.png
│
├── tasks_not_do.json
├── tasks_end.json
│
└── README.md
```

### Description

| Fichier | Description |
|---|---|
| `todo.py` | Logique principale de l'application |
| `todo_main.kv` | Interfaces et composants graphiques |
| `task_end.kv` | Interface liée aux tâches terminées |
| `app_icon.png` | Icône principale de Focusly |
| `check_icon.png` | Icône utilisée pour valider une tâche |
| `tasks_not_do.json` | Stockage local des tâches non terminées |
| `tasks_end.json` | Stockage local des tâches terminées |
| `README.md` | Documentation du projet |

---

## ⚙️ Installation

### 1. Cloner le projet

```bash
git clone https://github.com/HDark02/Focusly.git
```

Puis :

```bash
cd Focusly
```

### 2. Installer Python

Utilise une version récente de Python compatible avec Kivy.

Vérifie l'installation :

```bash
python --version
```

### 3. Installer Kivy

```bash
pip install kivy
```

### 4. Installer KivyMD

```bash
pip install kivymd
```

---

## ▶️ Lancer l'application

Depuis le dossier du projet :

```bash
python todo.py
```

L'application démarre avec :

```python
if __name__=="__main__":
    Todo().run()
```



---

## 💾 Stockage des données

Focusly fonctionne actuellement avec un stockage local basé sur des fichiers JSON.

Les tâches en cours sont enregistrées dans :

```text
tasks_not_do.json
```

Les tâches terminées peuvent être enregistrées dans :

```text
tasks_end.json
```

Cela permet d'utiliser l'application sans serveur ni base de données distante.

---

## 🔮 Fonctionnalités prévues

Le projet peut évoluer avec de nombreuses fonctionnalités :

- 🔔 Notifications de rappel
- 📆 Calendrier complet
- 🔎 Recherche de tâches
- 🏷️ Catégories
- 🎯 Priorités
- 🔥 Système de tâches récurrentes
- 📊 Statistiques de productivité
- 🌐 Synchronisation cloud
- 👤 Compte utilisateur
- ☁️ Sauvegarde en ligne
- 🔐 Verrouillage de l'application
- 🌓 Mode clair / sombre
- 🤖 Assistant intelligent
- 📱 Version Android optimisée
- 🔄 Synchronisation entre plusieurs appareils

---

## 📱 Version Android

L'objectif du projet est de transformer Focusly en véritable application Android.

Une future version pourra être construite avec **Buildozer** afin de générer un fichier APK :

```text
Focusly.apk
```

---

## 🎨 Identité visuelle

Focusly utilise principalement une identité :

- 🟣 Violet
- 🔵 Bleu
- ⚫ Bleu très sombre
- ⚪ Blanc

L'objectif est d'obtenir une apparence moderne, futuriste et orientée productivité.

---

## 🤝 Contribution

Les contributions sont les bienvenues.

Pour contribuer :

```bash
git clone https://github.com/HDark02/Focusly.git
```

Crée ensuite une nouvelle branche :

```bash
git checkout -b feature/nouvelle-fonctionnalite
```

Effectue tes modifications puis :

```bash
git add .
git commit -m "Ajout d'une nouvelle fonctionnalité"
git push origin feature/nouvelle-fonctionnalite
```

Tu peux ensuite créer une **Pull Request**.

---

## 📄 Licence

Ce projet peut être distribué sous licence **MIT**.

Ajoute un fichier `LICENSE` au dépôt si tu souhaites publier officiellement le projet sous cette licence.

---

## 👨‍💻 Auteur

**Alex Dynamo**

### Focusly

> *Organise. Priorise. Accomplis.*

⭐ Si tu apprécies le projet, pense à laisser une étoile au repository GitHub !
