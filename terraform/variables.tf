variable "accountsID" {
  description = "map"
  type        = map(string)
}

variable "permissionARN" {
  description = "map"
  type        = map(string)
}

variable "account_assignments" {
  type = list(object({
    account             = string
    permission_set_name = string
    permission_set_arn  = string
    principal_name      = string
    principal_type      = string
  }))
  default = []
}
