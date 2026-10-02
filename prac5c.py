Practical 5(c)

Push Docker Image to Docker Hub


Step 1: Open Command Prompt or VS Code Terminal

Run:

docker images

You should see something like:

REPOSITORY   TAG      IMAGE ID
flask-app    latest   a1b2c3d4e5f6

If you don't see flask-app, you need to build the image first:

docker build -t flask-app .


Step 2: Log in to Docker Hub

Run:

docker login

Enter:

- Username: Your Docker Hub username
- Password: Your Docker Hub password (or Personal Access Token if your account requires one)

If successful, you'll see:

Login Succeeded


Step 3: Check Which Account Is Logged In

Run:

docker info

Look for:

Username: yourusername

Make sure it matches your Docker Hub account.


Step 4: Tag Your Image

Suppose your Docker Hub username is:

nikhita123

Run:

docker tag flask-app nikhita123/flask-app:latest

Replace nikhita123 with your own Docker Hub username.


Step 5: Verify the Tag

Run:

docker images

You should now see something like:

REPOSITORY              TAG      IMAGE ID
flask-app               latest   a1b2c3d4e5f6
nikhita123/flask-app    latest   a1b2c3d4e5f6


Step 6: Push the Image

Run:

docker push nikhita123/flask-app:latest

Replace nikhita123 with your actual Docker Hub username.

If everything is correct, Docker will upload the image.


Step 7: Verify on Docker Hub

1. Open:

https://hub.docker.com/

2. Log in.

3. Click Repositories.

4. You should see flask-app listed.