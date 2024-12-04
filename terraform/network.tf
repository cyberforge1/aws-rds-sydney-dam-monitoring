# terraform/network.tf
# --------------------------------------------------
# Terraform configuration to create a VPC and Internet Gateway.
# --------------------------------------------------

resource "aws_vpc" "main_vpc" {
  cidr_block           = var.VPC_CIDR
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "dam-monitoring-vpc"
  }
}

resource "aws_internet_gateway" "main_igw" {
  vpc_id = aws_vpc.main_vpc.id

  tags = {
    Name = "dam-monitoring-igw"
  }
}
