Sources:

https://www.docker.com/blog/docker-github-actions/
https://github.com/docker/build-push-action
https://hub.docker.com/_/python
https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#pushing-container-images
https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#pulling-container-images
https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#building-container-images
https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry#tagging-container-images
https://docs.github.com/en/packages/managing-github-packages-using-github-actions-workflows/publishing-and-installing-a-package-with-github-actions#publishing-a-package-using-an-action
How to build:
```
docker build -t legendary_db .
```
How to run:
```
docker run legendary_db
```

How to run interactively
```
docker run -i legendary_db
```

Renames Docker image FROM ---> TO
```
docker tag legendary_db ghcr.io/jkrogsrud/legendary_db
```

This pushes it to ghcr.io
```
docker push ghcr.io/jkrogsrud/legendary_db
```
