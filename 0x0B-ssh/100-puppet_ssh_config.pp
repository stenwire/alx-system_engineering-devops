# Pupprt ssh configuration that you can connect to a server without typing a password

include stdlib
file_line { 'configured to use the private key /etc/ssh/ssh_config':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'configured to refuse to authenticate using a password':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}
