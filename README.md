# Terraform Deployment for Stateless Application (Containerized)

This repository contains Terraform code to deploy a stateless application using containerized code. This README provides instructions on how to set up and use this Terraform deployment.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your local machine:

- [Terraform](https://www.terraform.io/downloads.html)
- [Docker](https://docs.docker.com/get-docker/)
- [AWS CLI](https://aws.amazon.com/cli/)

## Usage

1. Clone the Repository from AWS Cloud shell:
   git clone https://github.com/datthu/infinitylabs.git
   cd infinitylabs
   
2. Initialize Terraform:
   Ensure the Terraform is properly install as per prerequisites
   cd terraform
   Run the following command to initialize Terraform in your project directory:
   terraform init

3. Terraform Validation:

   Run a Terraform plan to check the execution validation:
   terraform validate

7. Terraform Apply:

   Apply the Terraform configuration to create the infrastructure:
   terraform apply

8. Access Your Stateless Application:

   After Terraform completes the deployment, it will provide information about the created resources, including the URL for your stateless application. Access your application using this AWS URL.

9. Terraform Destroy (Optional):

   To tear down the infrastructure and terminate your application, run the following command:
   terraform destroy
