# Projet de Mise en Place d'une Solution d'Analyse Big Data

Ce projet a pour objectif de concevoir et d'implémenter une chaîne de traitement de données (pipeline Big Data) pour analyser les données climatiques historiques de la ville de Dakar. La solution couvre l'ensemble du cycle de vie de la donnée : de l'ingestion à la visualisation, en passant par le stockage et le traitement.

## 👥 Équipe du Projet

Ce projet a été réalisé en mars 2023 à l'ESMT, sous la supervision de M. Jean-Marie PREIRA.

* **Membres :**
* SANOGO Steve 
* BAZIE Dinin Lothaire 


## 🏗️ Architecture Technique

La solution repose sur une architecture Big Data intégrant les technologies suivantes:

* **Source de données :** API Open-Meteo (Données météorologiques).
* **Ingestion :** Filebeat (Collecte et transfert des logs/données).
* **Traitement (Processing) :** Apache Spark (Calcul distribué in-memory).
* **Visualisation :** Grafana (Tableaux de bord interactifs).


## 📊 Données

Les données exploitées sont les relevés climatiques horaires de la ville de Dakar sur une période de 20 ans (2002 à 2022).

* **Volume :** 184 080 lignes, 8 colonnes.
* **Format :** JSON (API) converti pour analyse.
* **Variables principales :** Température (°C), Humidité relative (%), Vitesse du vent (km/h), Pression (hPa), Précipitations (mm), et Code météo (WMO).



## ⚙️ Installation et Configuration

### 1. Ingestion des données (Filebeat)

Filebeat est utilisé avec le module `httpjson` pour récupérer les données depuis l'API Open-Meteo.

**Configuration `script.yml` :**

```yaml
filebeat.inputs:
- type: httpjson
  request.url: https://archive-api.open-meteo.com/v1/archive
  json.keys_under_root: true
  json.overwrite_keys: true
  processors:
    - decode_json_fields:
        fields: ["message"]
        target: ""
        overwrite_keys: false
    - drop_fields:
        fields: ["*"]
        ignore_missing: true
    - include_fields:
        fields: ["hourly"]
output.file:
  path: "/home/hadoop/"
  filename: dakar_weather_2002_2022

```

**Exécution :**

```bash
/etc/filebeat-8.6.2-linux-x86_64/filebeat -c /home/hadoop/sript.yml
```
### 2. Traitement des données (Apache Spark)

Spark est utilisé pour nettoyer et structurer les données brutes.

* **Transformations effectuées :**
* Création de colonnes temporelles : `day`, `month`, `year`.

* Typage des données (Conversion des String en Int, Float, Date, etc.).

### 3. Visualisation (Grafana)

Grafana est installé sur un serveur Linux (CentOS/RHEL) pour visualiser les métriques.

**Installation rapide :**

1. Créer le fichier de dépôt : `sudo vim /etc/yum.repos.d/grafana.repo`.
2. Installer Grafana : `sudo yum install grafana`.
3. Démarrer le service : `sudo service grafana-server start`.
4. Accéder à l'interface : `http://<IP_SERVEUR>:3000`.

## 📈 Résultats et Visualisations

Le tableau de bord Grafana permet d'observer les tendances climatiques suivantes :

* **Températures :** Évolution de la moyenne de température par année.
* **Précipitations :** Somme des précipitations (pluie en mm) par année.
* **Conditions Météo :** Répartition des codes WMO (Weathercode) sous forme de diagramme circulaire (ex: 47.14% pour le code 51 - Bruine).


## 📚 Ressources
* Cours Plateforme Big Data par Jean-Marie Preira.
* Documentation Open-Meteo.
* Documentation Elastic/Filebeat.