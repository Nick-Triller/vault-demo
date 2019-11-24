vault {
  address = "http://vault:8200"
  vault_agent_token_file = "/conf/agent/agent.token"
}

template {
  source = "/conf/template.ctmpl"
  destination = "/out/creds.txt"
}
