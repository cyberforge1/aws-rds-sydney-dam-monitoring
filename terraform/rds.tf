# terraform/rds.tf
# --------------------------------------------------
# Terraform configuration to create an AWS RDS instance
# with the lowest cost possible under the AWS Free Tier.
# --------------------------------------------------

provider "aws" {
  region = var.AWS_REGION
}

resource "aws_db_instance" "rds_instance" {
  identifier              = "dam-monitoring-db"  # Custom identifier
  allocated_storage       = 20
  max_allocated_storage   = 20
  engine                  = "mysql"
  engine_version          = "8.0.32"
  instance_class          = var.INSTANCE_CLASS
  db_name                 = var.DB_NAME
  username                = var.DB_USERNAME
  password                = var.DB_PASSWORD
  publicly_accessible     = true
  skip_final_snapshot     = true
  deletion_protection     = false
  backup_retention_period = 0

  tags = {
    Name = "dam-monitoring-rds"
  }
}


output "rds_endpoint" {
  value = aws_db_instance.rds_instance.endpoint
}

output "rds_username" {
  value = aws_db_instance.rds_instance.username
}
