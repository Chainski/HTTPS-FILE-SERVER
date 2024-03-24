<a href="https://github.com/chainski/HTTPS-FILE-SERVER"><img src="https://img.shields.io/badge/OPEN--SOURCE-YES-green"></a>
<a href="https://github.com/chainski/HTTPS-FILE-SERVER"><img src="https://img.shields.io/badge/PYTHON-3.10-green"></a>
<a href="https://github.com/chainski/HTTPS-FILE-SERVER"><img src="https://img.shields.io/badge/license-GPL--3.0-orange"></a> 
<a href="https://github.com/chainski/HTTPS-FILE-SERVER"><img src="https://img.shields.io/badge/contributions-welcome-green"></a>

# HTTPS-FILE-SERVER
- This is a simple http file server to access your files via webbrowser.

## Preview
![image](https://user-images.githubusercontent.com/96607632/157678533-bbd2a9ee-6d78-4d91-9efa-b2cfb615108e.png)

## Support Python Version
- Python 3.10+

## Dependencies
- run install.bat


## Why choose
- Good UI
- Lightweight
- SSL support
- Easy to use

## Usage
```
python https-file-server
```
## Mandatory SSL
This script must be used with a certificate in order to work so, you need to generate one:

## Open Powershell as admin and enter the command below
```
$cert = New-SelfSignedCertificate -Subject "localhost" -TextExtension @("2.5.29.17={text}DNS=localhost&IPAddress=127.0.0.1") -CertStoreLocation cert:\LocalMachine\My 
$pwd = ConvertTo-SecureString -String "httpfileserver" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath $env:userprofile\downloads\cert.pfx -Password $pwd
```
## Convert the .pfx file to a .pem extension using <a href="https://slproweb.com/products/Win32OpenSSL.html"><img src="https://img.shields.io/badge/Open-SSL-yellow"></a> 
```
openssl pkcs12 -in cert.pfx -out cert.pem -nodes

```
After converting the certificate move it to the same directory as the script then run 
```
python https-file-server.py 
```
