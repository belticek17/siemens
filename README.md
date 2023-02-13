# Siemens
Task for the jpb interview in Siemens: Python script that counts sin(x) for 1000 samples from 0 to 6pi and visualize it in some Dashboard and create a Docker image containing all the necessary components.

### Development
Docker should install all the dependencies and make the image, so run:
```bash
docker build -t myapp
```
It may take a while, just wait.  

Then you should be able to run the image:
```bash
docker run -it --rm myapp
```

You can also run:
```bash
docker-compose up
```
Done, now just visit https://6db5ed325d964206b2916236ed347474.us-central1.gcp.cloud.es.io:9243/app/r/s/4uPx2
