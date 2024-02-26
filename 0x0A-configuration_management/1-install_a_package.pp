# installing pip3 to use for flash and Werkzeug
package { 'python3-pip':
  ensure => installed,
}

# automating installition of flask 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# automating installition of Werkzeug 2.2.1
package { 'Werkzeug':
  ensure   => '2.2.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
