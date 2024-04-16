#fix 500 error on server.

exec{
    command => 'bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
