# terraform/security_group.tf
# --------------------------------------------------
# Terraform configuration to create a Security Group for RDS.
# --------------------------------------------------

resource "aws_security_group" "rds_sg" {
  name        = "dam-monitoring-rds-sg"
  description = "Security group for Dam Monitoring RDS instance"
  vpc_id      = aws_vpc.main_vpc.id

  ingress {
    description      = "Allow MySQL traffic from specified CIDR blocks"
    from_port        = 3306
    to_port          = 3306
    protocol         = "tcp"
    cidr_blocks      = var.ALLOWED_CIDR_BLOCKS
    ipv6_cidr_blocks = ["::/0"]  # Optional: Allows IPv6 access
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"  # All traffic
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "dam-monitoring-rds-sg"
  }
}
