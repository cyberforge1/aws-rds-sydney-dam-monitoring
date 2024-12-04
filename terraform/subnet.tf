# terraform/subnet.tf
# --------------------------------------------------
# Terraform configuration to create Public Subnets and Route Tables.
# --------------------------------------------------

resource "aws_subnet" "public_subnet_a" {
  vpc_id            = aws_vpc.main_vpc.id
  cidr_block        = var.PUBLIC_SUBNET_A_CIDR
  availability_zone = "${var.AWS_REGION}a"

  tags = {
    Name = "dam-monitoring-public-subnet-a"
  }
}

resource "aws_subnet" "public_subnet_b" {
  vpc_id            = aws_vpc.main_vpc.id
  cidr_block        = var.PUBLIC_SUBNET_B_CIDR
  availability_zone = "${var.AWS_REGION}b"

  tags = {
    Name = "dam-monitoring-public-subnet-b"
  }
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.main_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main_igw.id
  }

  tags = {
    Name = "dam-monitoring-public-rt"
  }
}

resource "aws_route_table_association" "public_rt_assoc_a" {
  subnet_id      = aws_subnet.public_subnet_a.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "public_rt_assoc_b" {
  subnet_id      = aws_subnet.public_subnet_b.id
  route_table_id = aws_route_table.public_rt.id
}
