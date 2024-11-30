# Commands

# VENV

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt



# Scripts

## Local DB

python3 scripts/local_db_connect.py

python3 scripts/local_db_seeding.py

python3 scripts/local_run_queries.py



## AWS RDS

python3 scripts/aws_rds_connect.py



# Terraform

terraform -chdir=terraform plan

terraform -chdir=terraform apply

terraform -chdir=terraform destroy