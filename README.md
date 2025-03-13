# AWS SAM CRUD

Ce projet implémente une API CRUD pour gérer des produits en utilisant **AWS SAM** (Serverless Application Model). L'architecture repose sur **API Gateway, AWS Lambda et Amazon DynamoDB**.

## 📌 Architecture

L'architecture suit le schéma suivant :
- **Amazon API Gateway** : Expose les endpoints REST pour l'accès utilisateur.
- **AWS Lambda** : Gère la logique métier pour les opérations CRUD.
- **Amazon DynamoDB** : Stocke les données des produits.

### 🔗 Flux des requêtes
1. L'utilisateur envoie une requête à l'API via **API Gateway**.
2. API Gateway invoque une **fonction AWS Lambda** en fonction de l'opération demandée (Create, Read, Update, Delete).
3. La fonction Lambda interagit avec **DynamoDB** pour lire ou modifier les données.

## 🛠️ Déploiement

### 🔧 Prérequis
- **AWS CLI** installé et configuré
- **AWS SAM CLI** installé ([Installation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html))
- **Docker** (optionnel, pour les tests locaux)
- **Git** installé

### 🚀 Étapes d'installation

1. **Cloner le repo**
   ```bash
   git clone https://github.com/hibarbel/aws_sam_crud.git
   cd aws_sam_crud
