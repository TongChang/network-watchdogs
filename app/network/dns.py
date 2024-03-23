def get_dns_server(force_google=True):
    if (force_google):
        return "8.8.8.8"
    else:
        try:
            with open('/etc/resolv.conf', 'r') as f:
                dns_servers = [line.strip().split(' ')[1] for line in f if line.startswith('nameserver')]
                return dns_servers[0]
        except Exception as e:
            return ""
