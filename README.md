# Serverless API on AWS with Terraform, Lambda, API Gateway, and DynamoDB

## Project Overview
This project provisions a production-ready, highly scalable serverless backend on Amazon Web Services (AWS) using Terraform as the Infrastructure as Code (IaC) tool. The architecture eliminates server management overhead, automatically scaling compute and database resources on-demand while maintaining low operational costs through a pay-per-request pricing model.

---

## Architecture Components

* **Amazon API Gateway (HTTP API):** Acts as the high-performance public entry point, routing incoming HTTP requests to the backend compute layer with minimal latency.
* **AWS Lambda (Python 3.11):** Executes the serverless business logic on-demand. It handles incoming HTTP methods (POST and GET), processes JSON payloads, and interfaces with the database.
* **Amazon DynamoDB:** A fully managed NoSQL key-value database configured with on-demand billing (`PAY_PER_REQUEST`) to store application items reliably.
* **AWS IAM Least-Privilege Execution Role:** Restricts the Lambda function permissions strictly to necessary operations—specifically CloudWatch logging and DynamoDB read/write access—adhering to cloud security best practices.

---

## Project Directory Structure

```text
aws-serverless-api/
├── lambda/
│   └── handler.py          # Python source code for the serverless function
├── .gitignore              # Specifies intentionally untracked build and state files
├── main.tf                 # Core infrastructure definitions (DynamoDB, Lambda, IAM, API Gateway)
├── outputs.tf              # Exposes public API Gateway endpoints after deployment
├── providers.tf            # Provider version requirements and AWS region configurations
└── terraform.tfstate       # Local state file tracking provisioned resources

## Practice Section
This section was added via a separate git branch to test merging workflows.