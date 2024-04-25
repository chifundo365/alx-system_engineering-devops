# configures ss configuration file
file { '~/.ssh/config':
  ensure  => file,
  content => 'Host remote_server\n\s\s\s\sHostName 34.224.16.226\n\s\s\s\s User ubuntu\n\s\s\s\sIdentityFile ~/.ssh/school',
}
