# Terraform Deployment for Stateless Application (Containerized)

This repository contains Terraform code to deploy a stateless application using containerized code. This README provides instructions on how to set up and use this Terraform deployment.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your local machine:

- [Terraform](https://www.terraform.io/downloads.html)
- [Docker](https://docs.docker.com/get-docker/)
- [AWS CLI](https://aws.amazon.com/cli/)

## Usage

1. Clone the Repository:

   git clone https://github.com/datthu/infinitylabs.git
   cd infinitylabs
   
2. Initialize Terraform:

   Run the following command to initialize Terraform in your project directory:
   terraform init

3. Configuration:

   Update the variables.tf file with your desired configuration, including AWS region, container image details, and any other variables specific to your application.

4. Terraform Plan:

   Run a Terraform plan to check the execution plan:
   terraform plan

5. Terraform Apply:

   Apply the Terraform configuration to create the infrastructure:
   terraform apply

6. Access Your Stateless Application:

   After Terraform completes the deployment, it will provide information about the created resources, including the URL for your stateless application. Access your application using this URL.

7. Terraform Destroy (Optional):

   To tear down the infrastructure and terminate your application, run the following command:
   terraform destroy
