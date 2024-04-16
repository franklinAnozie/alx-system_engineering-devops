#fix 500 error on server.

exec{ 'replace all occrance on phpp with php':
    command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
    path => '/bin:/usr/bin'
}
