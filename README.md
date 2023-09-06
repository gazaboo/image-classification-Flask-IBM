# Exemple Pedagogique utilisant docker-compose  

## Containers : 
- **Serveur Flask** créé à la main et conteuneurisé. 
Il permet d'uploader des images qui sont renvoyées à un second container. 

- Un container issu d'une image créée par IBM
[ Inception-ResNet-v2 Image Classifier ] -> classifieur d'image (deep learning) via une API. 

## Remarques : 
- Les volumes sont mappés et le serveur Flask en mode debug. Vous pouvez observer les changements en temps réel.  
- Pour lancer le projet : **sudo docker-compose up**