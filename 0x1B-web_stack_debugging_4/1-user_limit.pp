#making user limitless

exec { 'increase access level of user':
    command => 'sed -i "/^holberton/s/[0-9]$/10000/" /etc/security/limits.conf',
    path    => '/bin:/usr/bin'
}
