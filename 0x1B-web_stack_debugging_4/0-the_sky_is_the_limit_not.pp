#making our server accept max requests

exec { 'increase ulimit to 4096':
    command => 'sed -i "s/15/4096/g" /etc/default/nginx',
    path    => '/bin:/usr/bin'
}

exec { 'restart the server':
    command => 'service nginx restart',
    path    => '/bin:/usr/bin'
}
