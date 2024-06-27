# Fix apache webserver 500 server error response

exec {'replace_file_extention':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
