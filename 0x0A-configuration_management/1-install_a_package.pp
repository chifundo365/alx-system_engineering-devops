# installs flask from pip3, version 2.1.0
exec { 'install_flask':
  command => '/usr/bin/env pip3 install Flask==2.0.1',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/env pip3 show flask | grep -q "Version: 2.1.0"',
}
