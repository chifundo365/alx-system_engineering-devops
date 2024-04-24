# kills a process named 'killmenow'
exec { 'kill_process':
  command => '/usr/bin/pkill -9 killmenow',
  path    => ['/usr/bin'],
}
