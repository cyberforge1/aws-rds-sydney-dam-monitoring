# terraform/variables.tf
# --------------------------------------------------
# Variables for AWS RDS Terraform configuration.
# --------------------------------------------------

variable "AWS_REGION" {
  type        = string
  description = "The AWS region to deploy resources"
  default     = "us-east-1"
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
  default     = "StrongPassword123!"
  sensitive   = true  # Marks the variable as sensitive to prevent it from being displayed in logs and outputs
}

variable "INSTANCE_CLASS" {
  type        = string
  description = "The instance class for the RDS instance. Example: db.t2.micro, db.t3.micro, db.t4g.micro"
  default     = "db.t3.micro"  # Updated default
}
