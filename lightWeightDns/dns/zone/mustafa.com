$ttl 86400
@       IN      SOA ns.mustafa.com. hostmaster.mustafa.com.(
                    202 ; Serial
                    600 ; Refresh
                    3600 ; Retry
                    1209600  ; Expire
                    3600)    ; Negative Cache TTL

@       IN      ns  ns.mustafa.com.
ns      IN      A   127.0.0.1