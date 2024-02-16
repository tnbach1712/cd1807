resource "azurerm_network_interface" "ni-test" {
  name                = "ni-test"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip_address_id}"
  }
}

resource "azurerm_linux_virtual_machine" "vm-test" {
  name                = "vm-test"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS2_v2"
  admin_username      = "${var.admin_username}"
  network_interface_ids = [ resource.azurerm_network_interface.ni-test.id ]
  admin_ssh_key {
    username   = "${var.admin_username}"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCarI+tvMmCBi+ORmW6EaatJ6B8twhDEfyAkGVYW4eQSP93Lu5GasN/dorjFyQc6ieicybbTYTO0LF+w/qyKqgR7maC1aT3Gu5CXk0Z7h9gbk2XCePRbWajOvTWAur/BQOk7Qjoj2Qx0HM2gOI1SrWZfeYTJ5THyeACPllmgv7+q1CPEdLeutgUKrRf9zAmQx7Ztl9pfEr1CN7Dg/YRX9ZXG5MUsGzC48x5DyniZLbLJwW0AKHvXHbcPbhsFxisqgF6WAUXzDZ5dO+gsuAVTbg9E+8N0mRgDOvKVKeXnaDCcsMZ4/RHCBD16kqwHADzz+56jLq3n7X7Vn5ROASdAqMDBpdkUOGmQUaZYlzVd9MHGpe595/6EnRVXXMfxFg16a5o2Cbsxu8GtS+GI0b09p+3euyXsYOf+yG07AOuxvXqHt+3rUErdQSxpWhwqlkTKvUmqDPsS+Pk1bfCngo6oBXx/nbrHODTSBY9NxRKPxMBrEejeD5XdrMHXfJTsqwvCjs= thekop@thekop"

  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
