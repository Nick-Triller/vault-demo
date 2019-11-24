exit_after_auth = false

vault {
  address = "http://vault:8200"
}

auto_auth {
  method "approle" {
    mount_path = "auth/approle"
    config = {
      role_id_file_path = "/conf/vault/role-id.txt"
      secret_id_file_path = "/conf/vault/secret-id.txt"
      remove_secret_id_file_after_reading = false
    }
  }

  sink "file" {
    config = {
      path = "/out/agent.token"
    }
  }
}
