# terraform/db_subnet_group.tf
# --------------------------------------------------
# Terraform configuration to create a DB Subnet Group for RDS.
# --------------------------------------------------

resource "aws_db_subnet_group" "rds_subnet_group" {
  name       = "dam-monitoring-db-subnet-group"
  subnet_ids = [
    aws_subnet.public_subnet_a.id,
    aws_subnet.public_subnet_b.id
  ]

  tags = {
    Name = "dam-monitoring-db-subnet-group"
  }
}
