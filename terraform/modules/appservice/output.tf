output "web_app_default_hostname" {
  value = azurerm_linux_web_app.test.default_site_hostname
}

output "web_app_outbound_ip_addresses" {
  value = azurerm_linux_web_app.test.outbound_ip_addresses
}

output "web_app_resource_id" {
  value = azurerm_linux_web_app.test.id
}

output "app_service_name" {
  value = azurerm_linux_web_app.test.name
}