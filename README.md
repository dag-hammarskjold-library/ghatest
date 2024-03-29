# ghatest

A minimal web application that has several CI/CD deployment options so we can test different strategies.

## Strategies

1. Docker, to deploy to, e.g., AWS ECS, using an ECR image
2. Serverless (AWS Lambda)
3. SSH to a target machine, e.g., AWS EC2

Additionally, the following will be included:
1. Semantic Release (available for both Python and JS applications)
2. Automated tests with pytest for issued PRs (i.e., Continuous Integration)
3. Automated deployment (branch, release) via GitHub Actions (Continuous Delivery)

## Docker

This just builds an image and runs it in a container listening on port 5000, serving the "dev" application. 
Change the arguments (port, environment) to match your needs.

Build: `docker buildx build -t ghatest .`

Run: `docker run -e FLASK_ENV=dev --rm -p 5000:5000 ghatest`