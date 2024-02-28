# updating apt
exec { 'apt-get update':
  path        => '/usr/bin',
  refreshonly => true,
}

# installing nginx
package { 'nginx':
  ensure => 'latest',
  notify => Exec['apt-get update'],
}

# adding hello world to a new file index.html
file { '/var/www/html/index.html':
  ensure  => file,
  owner   => root,
  group   => root,
  mode    => '0644',
  replace => true,
  content => 'Hello World!
',
}

# string to add to the default file
$config = 'server {
        listen 80 default_server;
        listen [::]:80 default_server;


        root /var/www/html;

        # Add index.php to the list if you are using PHP
        index index.html index.htm index.nginx-debian.html;

        server_name ajwadg.tech;

        location /redirect_me {
                return 301 https://www.nginx.com/blog/creating-nginx-rewrite-rules/;
        }
}'


file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  replace => true,
  content => $config,
}


# restarting nginx
exec { 'service -y nginx':
  command => '/usr/sbin/service nginx restart',
}
