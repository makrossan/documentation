---
title: "docker-compose - Keycloak with SSL enabled."
date: 2025-09-13T19:33:59.000Z
slug: docker-compose-keycloak-with-ssl-enabled
---

If you have an SSL certificate in CRT format and you want to use it with
Keycloak running in Docker, you will need to create a Java keystore file
(typically JKS or PKCS12 format) that includes your certificate. Below
are the steps to create a PKCS12 keystore using your existing CRT file
along with its corresponding private key. Then I’ll show you how to
update your Docker command accordingly.

### Steps to Create a PKCS12 Keystore

1.  **Prepare Your Certificate Files:**
    - Ensure you have your certificate file (`.crt`) and your private
      key file (`.key`).
    - If you have any intermediate certificates or a chain certificate,
      make sure these are also ready.
2.  **Combine Your Certificates into a Single File (if necessary):** If
    you have a chain of certificates (e.g., your certificate plus any
    intermediate CA certificates), concatenate them into a single
    file:bash`cat your_certificate.crt intermediate_certificate.crt > combined_certificates.crt`
3.  **Create a PKCS12 Keystore:** You’ll need the OpenSSL tool to
    execute this step, combining your private key and the certificate(s)
    into a PKCS12
    keystore:`openssl pkcs12 -export -out keystore.p12 -inkey private_key.key -in combined_certificates.crt -name keycloak`Replace
    `private_key.key` with your private key file, and
    `combined_certificates.crt` with your certificate file or combined
    certificate file. The `-name keycloak` is the alias for your key
    entry, which you can customize as needed.
4.  **Move the Keystore to the Appropriate Directory:** Move the
    generated `keystore.p12` file to the directory that will be mounted
    into the Docker
    container:`mv keystore.p12 /home/admin1/dockervol/keycloak/data/`

### Update Your Docker Run Command

After creating the keystore, you can modify your Docker command to use
this keystore for enabling SSL:

``` bash
docker run -d -it --name keycloak \ -p 3085:8443 \ -v /home/admin1/dockervol/keycloak/data:/opt/jboss/keycloak/standalone/data \ -e KEYCLOAK_ADMIN=admin \ -e KEYCLOAK_ADMIN_PASSWORD=admin \ -e KEYCLOAK_HTTPS_PORT=8443 \ -e KEYCLOAK_HTTP_PORT=8080 \ -e KEYCLOAK_HOSTNAME=localhost \ -e KEYCLOAK_SSL_REQUIRED=external \ -e KEYCLOAK_USER_SSL_CERTIFICATE_FILE=/opt/jboss/keycloak/standalone/data/keystore.p12 \ -e KEYCLOAK_USER_SSL_CERTIFICATE_KEYSTORE_TYPE=PKCS12 \ -e KEYCLOAK_USER_SSL_CERTIFICATE_KEYSTORE_PASSWORD=[your_keystore_password] \ quay.io/keycloak/keycloak:24.0.2 start-dev
```

**Key changes made:**

- **Port Mapping:** Adjusted to `3085:8443` to reflect the SSL
  configuration.
- **Environment Variables:** Added for SSL setup, where
  `[your_keystore_password]` should be replaced with the password you
  specified when creating the keystore.

This command configures Keycloak to use HTTPS with the specified SSL
certificate. Always test the configuration in a development environment
before applying it to production to ensure all settings are correct and
the application is secure.
