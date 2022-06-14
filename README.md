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

### Support and Contributions
My software is open source and free for public use. 
If you found any of these repos useful and would like to support this project financially, 
feel free to donate to my bitcoin address.
### 16T1fUehoGR4E2sj98u9e9mKuQ7uSLvxRJ
![image](https://user-images.githubusercontent.com/96607632/173610346-a08309b7-7ce5-4be8-88f2-d79cb6e9c3bf.png)
