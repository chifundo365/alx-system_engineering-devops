file { '/root/.ssh/config':
  ensure  => file,
  content => "Host remote_server\n\
    HostName 34.224.16.226\n\
    User ubuntu\n\
    IdentityFile ~/.ssh/school\n",
}
