# terraform/variables.tf
# --------------------------------------------------
# Variables for AWS RDS Terraform configuration.
# --------------------------------------------------

variable "AWS_REGION" {
  type        = string
  description = "The AWS region to deploy resources"
  default     = "ap-southeast-2"  # Update as needed
}

variable "AWS_ACCOUNT_ID" {
  type        = string
  description = "The AWS Account ID"
}

variable "DB_NAME" {
  type        = string
  description = "The name of the RDS database"
  default     = "dam_monitoring_db"
}

variable "DB_USERNAME" {
  type        = string
  description = "The master username for the RDS instance"
  default     = "admin"
}

variable "DB_PASSWORD" {
  type        = string
  description = "The master password for the RDS instance"
  default     = "StrongPassword123!"  # Replace with a secure password
  sensitive   = true  # Marks the variable as sensitive
}

variable "INSTANCE_CLASS" {
  type        = string
  description = "The instance class for the RDS instance. Example: db.t2.micro, db.t3.micro, db.t4g.micro"
  default     = "db.t3.micro"
}

variable "VPC_CIDR" {
  type        = string
  description = "The CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "PUBLIC_SUBNET_A_CIDR" {
  type        = string
  description = "CIDR block for Public Subnet A"
  default     = "10.0.1.0/24"
}

variable "PUBLIC_SUBNET_B_CIDR" {
  type        = string
  description = "CIDR block for Public Subnet B"
  default     = "10.0.2.0/24"
}

variable "ALLOWED_CIDR_BLOCKS" {
  type        = list(string)
  description = "List of CIDR blocks allowed to access the RDS instance"
  default     = ["0.0.0.0/0"]  # ⚠️ Allows access from anywhere
}
