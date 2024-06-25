$ttl 86400
@       IN      SOA ns.farouq.com. hostmaster.farouq.com.(
                    202 ; Serial
                    600 ; Refresh
                    3600 ; Retry
                    1209600  ; Expire
                    3600)    ; Negative Cache TTL

@       IN      ns  ns.farouq.com.
ns      IN      A   127.0.0.1