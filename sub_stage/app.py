import cx_Oracle
import pyodbc
import selenium
import os
import subprocess
import ldap
import gssapi

try:
    print("==========Selenium Part==========")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com")

    search_box = driver.find_element("name","q")
    search_box.send_keys("Python Selenium")

    search_box.submit()
    print(driver.page_source)

    driver.quit()


    # --------  ORACLE Server Connection --------- #
    print(print("==========Oracle Part=========="))

    # Replace these values with your actual database connection details
    hostname = "oracledb"
    port = 1521
    service_name = "XE"
    username = "system"
    password = "oracle"
    mode = cx_Oracle.SYSDBA
    sid = 'XE'

    # Connection parameters
    # dsn = 'oracledb:1521/USERS'  # Format: hostname:port/service_name

    # cx_Oracle.init_oracle_client(lib_dir=os.getenv('LD_LIBRARY_PATH'))

    dsn_tns = cx_Oracle.makedsn(hostname,port,service_name = service_name)


    # Establish connection
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns)

    # Create cursor
    cursor = connection.cursor()

    # Execute SQL query
    cursor.execute("SELECT tablespace_name AS database_name FROM user_tablespaces")

    # Fetch results
    for row in cursor:
        print(row)

    # Close cursor and connection
    cursor.close()
    connection.close()


    # --------  LDAP Connection --------- #
    print(print("==========LDAP Part=========="))

    # LDAP connection details
    ldap_url = "ldap://openldap7:1389"
    ldap_user = "cn=admin,dc=test777,dc=com"
    ldap_password = "P@ssw0rd"
    ldap_base_dn = "dc=test777,dc=com"
    ldap_filter = "(objectclass=*)"
    ldap_scope = ldap.SCOPE_SUBTREE
    new_username = 'mustafa'

    # Establish LDAP connection
    ldap_conn = ldap.initialize(ldap_url)
    ldap_conn.simple_bind_s(ldap_user, ldap_password)

    # Perform LDAP search
    search_result = ldap_conn.search_s(ldap_base_dn, ldap_scope, ldap_filter)

    # Print search result
    for dn, entry in search_result:
        print("DN:", dn)
        print("Entry:", entry)

    # Modify the username
    modify_attrs = [(ldap.MOD_REPLACE, 'cn', new_username.encode('utf-8'))]
    ldap_conn.modify_s('cn=mustafa,ou=users,dc=test777,dc=com', modify_attrs)

    # Close LDAP connection
    ldap_conn.unbind()
    print(f"Username changed successfully to: {new_username}")


    print("==========Kerberos==========")

    server_name = gssapi.Name('krbtgt/DOMAIN.COM@')

    username = "root/admin"
    password = "P@ssw0rd"

    user = gssapi.Name(base=username, name_type=gssapi.NameType.user)
    bpass = password.encode('utf-8')
    result = False
    try:
        creds = gssapi.raw.acquire_cred_with_password(user, bpass, usage='initiate')
        creds = creds.creds
        context = gssapi.SecurityContext(name=server_name, creds=creds, usage='initiate')
        result = True
    except AttributeError:
        print("AttributeError")
    except gssapi.exceptions.GSSError as er:
        print(er)
    # acquire_cred_with_password returns a wrapper, we want the creds
    # object inside this wrapper
    print(result)

    # --------  SQL Server Connection --------- #
    print(print("==========MSSQL Part=========="))
    # Connect to the SQL Server database

    # Establish connection to SQL Server
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            'SERVER=mssqldb,1433;'
                            'DATABASE=master;'
                            'UID=sa;'
                            'PWD=P@ssw0rd;'
                            'TrustServerCertificate=yes;'
                            'autocommit=True;')

    # Create a cursor object
    cursor = conn.cursor()

    # Check if the database exists
    cursor.execute("SELECT NAME FROM sys.databases")
    
    # Fetch results
    for row in cursor:
        print(row)

    # Close the cursor and connection
    conn.close()


except  Exception as e:
    print("Error occurred: ",e)

print("Hello Mustafa, If you reach out to this point, You already success, Congrats!!!")