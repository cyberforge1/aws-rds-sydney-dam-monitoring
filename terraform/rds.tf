# terraform/rds.tf
# --------------------------------------------------
# Terraform configuration to create an AWS RDS instance
# with explicit Security Groups and Subnets.
# --------------------------------------------------

provider "aws" {
  region = var.AWS_REGION
}

resource "aws_db_instance" "rds_instance" {
  identifier              = "dam-monitoring-db"
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

  vpc_security_group_ids = [aws_security_group.rds_sg.id]
  db_subnet_group_name   = aws_db_subnet_group.rds_subnet_group.name

  tags = {
    Name = "dam-monitoring-rds"
  }
}

output "rds_endpoint" {
  description = "The endpoint of the RDS instance"
  value       = aws_db_instance.rds_instance.endpoint
}

output "rds_username" {
  description = "The master username of the RDS instance"
  value       = aws_db_instance.rds_instance.username
}
