# Commands

# VENV

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt



# Scripts

## Local DB

python3 scripts/local_db/local_db_create_db.py

python3 scripts/local_db/local_db_connect.py

python3 scripts/local_db/local_db_create_schema.py

python3 scripts/local_db/local_db_seed_data.py

python3 scripts/local_db/local_db_test_queries.py




## AWS RDS

python3 scripts/aws_rds/aws_rds_connect.py

python3 scripts/aws_rds/aws_rds_create_schema.py

python3 scripts/aws_rds/aws_rds_seed_data.py

python3 scripts/aws_rds/aws_rds_test_queries.py


# Terraform

terraform -chdir=terraform plan

terraform -chdir=terraform apply

terraform -chdir=terraform destroy