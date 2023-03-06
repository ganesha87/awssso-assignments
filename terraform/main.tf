# ---------------------------------------------
###  Terraform and providers Section     ###
# ---------------------------------------------
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.26.0"
    }
  }
}

#-----------------------------------------------------------------------------------------------------------------------
# CREATE / UPDATE THE ASSIGNMENTS
#-----------------------------------------------------------------------------------------------------------------------
resource "aws_ssoadmin_account_assignment" "this" {
  for_each = local.assignment_map

  instance_arn       = local.sso_instance_arn
  permission_set_arn = lookup(var.permissionARN,each.value.permission_set_arn,"no-permission_set_arn")
  
  principal_id   = data.aws_identitystore_group.this[each.value.principal_name].id
  principal_type = each.value.principal_type

  target_id   = lookup(var.accountsID,each.value.account,"no-account")
  target_type = "AWS_ACCOUNT"
}

#-----------------------------------------------------------------------------------------------------------------------
# LOCAL VARIABLES AND DATA SOURCES
#-----------------------------------------------------------------------------------------------------------------------

data "aws_ssoadmin_instances" "this" {}

locals {
    identity_store_id = tolist(data.aws_ssoadmin_instances.this.identity_store_ids)[0]
    sso_instance_arn  = tolist(data.aws_ssoadmin_instances.this.arns)[0]
}

locals {
  assignment_map = {
    for a in var.account_assignments :
    format("%v-%v-%v-%v", a.account, substr(a.principal_type, 0, 1), a.principal_name, a.permission_set_name) => a
  }

  group_list = toset([for mapping in var.account_assignments : mapping.principal_name if mapping.principal_type == "GROUP"])
}

data "aws_identitystore_group" "this" {
  for_each          = local.group_list
  identity_store_id = local.identity_store_id

  alternate_identifier {
    unique_attribute {
      attribute_path  = "DisplayName"
      attribute_value = each.key
    }
  }
}
